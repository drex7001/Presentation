from manim import *

# --- Custom Component (The "Class" for our boxes) ---
class ArchitectureBlock(VGroup):
    """
    A reusable component to create the rectangular blocks in the diagram.
    This acts like a React Component.
    """
    def __init__(self, label_text, sub_text="", width=3.5, height=1.5, color=WHITE, font_size=20, **kwargs):
        super().__init__(**kwargs)
        
        # The Rectangle (The Container)
        self.box = Rectangle(width=width, height=height, color=color)
        self.box.set_fill(color, opacity=0.1) # Slight background fill
        
        # The Main Label (Title)
        self.label = Text(label_text, font_size=font_size, color=color, weight=BOLD)
        
        # The Sub Label (Description/Tools) - Optional
        if sub_text:
            self.sub_label = Text(sub_text, font_size=14, color=GRAY, slant=ITALIC)
            # Group title and subtitle vertically
            text_group = VGroup(self.label, self.sub_label).arrange(DOWN, buff=0.15)
        else:
            text_group = self.label

        # Center the text inside the box
        text_group.move_to(self.box.get_center())
        
        # Add everything to the VGroup
        self.add(self.box, text_group)

# --- The Main Scene ---
class FullArchitectureMap(MovingCameraScene):
    def construct(self):
        # self.add(NumberPlane())
        # Set the camera to zoom out slightly so everything fits
        self.camera.frame.scale(1.7)

        # --- STEP 1: DEFINE THE NODES (OBJECTS) ---
        
        # 1. Input Layer (Left side)
        input_block = ArchitectureBlock(
            "Input Handler", 
            "Images, Text, Voice\n(Standardized to Text)", 
            color=BLUE, 
            height=4
        )
        
        # 2. Guardrails
        guardrail_block = ArchitectureBlock(
            "Guardrails", 
            "Relevance & Jailbreak", 
            color=RED,
            width=2.5
        )
        
        # 3. Triage Agent (The Router)
        triage_block = ArchitectureBlock(
            "Triage Agent", 
            "Intent Classification", 
            color=WHITE,
            width=2.5
        )

        # 4. Special Handling (Top Branch)
        direct_block = ArchitectureBlock("Direct Handling", "Greetings, Spam", width=2.5, height=1, color=YELLOW)
        handoff_block = ArchitectureBlock("Human Handoff", "Angry/Upset Sentiment", width=2.5, height=1, color=ORANGE)

        # 5. Core Agents (The "Fast Lanes")
        sales_block = ArchitectureBlock("Sales Agent", "Pre-purchase & Product Info", color=GREEN)
        ops_block = ArchitectureBlock("OPS Agent", "Order Tracking & Status", color=TEAL)
        support_block = ArchitectureBlock("Support Agent", "Returns & Post-purchase", color=PURPLE)

        # 6. Finalizer (Right side)
        finalize_block = ArchitectureBlock("Finalize Agent", "Format Response", color=GOLD, width=2.5)

        # --- STEP 2: POSITIONING (LAYOUT) ---
        
        # Place Triage in the approximate center-left
        triage_block.shift(LEFT * 1)
        
        # Guardrail is to the left of Triage
        guardrail_block.next_to(triage_block, LEFT, buff=1)
        
        # Input is to the left of Guardrail
        input_block.next_to(guardrail_block, LEFT, buff=1)

        # Position Core Agents (Sales, OPS, Support) vertically to the right of Triage
        ops_block.next_to(triage_block, RIGHT, buff=2) # Middle one first
        sales_block.next_to(ops_block, UP, buff=0.5)   # Top one
        support_block.next_to(ops_block, DOWN, buff=0.5) # Bottom one
        
        # Position Special Handling (Direct/Handoff) above Triage/Guardrails
        direct_block.move_to(sales_block.get_center() + UP * 1.8) # Above Sales
        handoff_block.next_to(direct_block, LEFT, buff=0.5)

        # Position Finalizer to the right of the agents
        finalize_block.next_to(ops_block, RIGHT, buff=2)

        # --- STEP 3: CREATING CONNECTIONS (ARROWS) ---
        
        # Main Flow Arrows
        arrow_1 = Arrow(input_block.get_right(), guardrail_block.get_left())
        arrow_2 = Arrow(guardrail_block.get_right(), triage_block.get_left())

        # Branching Arrows (Triage -> Agents)
        # We use 'start' and 'end' points for cleaner lines
        arrow_sales = Arrow(triage_block.get_right(), sales_block.get_left(), color=GRAY)
        arrow_ops = Arrow(triage_block.get_right(), ops_block.get_left(), color=GRAY)
        arrow_support = Arrow(triage_block.get_right(), support_block.get_left(), color=GRAY)
        
        # Special Handling Arrows (Curved lines look better for top branches)
        arrow_direct = CurvedArrow(triage_block.get_top(), direct_block.get_left(), color=YELLOW, angle=-TAU/8)
        arrow_handoff = CurvedArrow(triage_block.get_top(), handoff_block.get_bottom(), color=ORANGE, angle=TAU/8)

        # Finalizing Arrows (Agents -> Finalizer)
        arrow_to_final_1 = Arrow(sales_block.get_right(), finalize_block.get_left(), color=GRAY)
        arrow_to_final_2 = Arrow(ops_block.get_right(), finalize_block.get_left(), color=GRAY)
        arrow_to_final_3 = Arrow(support_block.get_right(), finalize_block.get_left(), color=GRAY)

        # Labeling the branches (Optional but helpful)
        label_sales = Text("Pre-purchase", font_size=14).next_to(arrow_sales, UP, buff=0)
        label_ops = Text("Order Queries", font_size=14).next_to(arrow_ops, UP, buff=0)

        # --- STEP 4: ANIMATION SEQUENCE ---
        all_elements = VGroup(
            input_block, guardrail_block, triage_block,
            direct_block, handoff_block,
            sales_block, ops_block, support_block, finalize_block,
            arrow_1, arrow_2, arrow_sales, arrow_ops, arrow_support, arrow_direct, arrow_handoff, arrow_to_final_1, arrow_to_final_2, arrow_to_final_3,
        )

        all_elements.move_to(ORIGIN)

        # 1. Draw the Main Pipeline (Input -> Triage)
        self.play(Create(input_block))
        self.play(GrowArrow(arrow_1), Create(guardrail_block))
        self.play(GrowArrow(arrow_2), Create(triage_block))
        
        self.wait(0.5)

        # 2. Reveal the "Brains" (The Agents)
        # Using LaggedStart to make them appear one by one smoothly
        self.play(
            LaggedStart(
                Create(sales_block),
                Create(ops_block),
                Create(support_block),
                lag_ratio=0.3
            )
        )
        
        # 3. Connect them
        self.play(
            GrowArrow(arrow_sales), Write(label_sales),
            GrowArrow(arrow_ops), Write(label_ops),
            GrowArrow(arrow_support)
        )

        # 4. Show Edge Cases (Direct/Handoff)
        self.play(Create(direct_block), Create(handoff_block))
        self.play(Create(arrow_direct), Create(arrow_handoff))

        # 5. Show Finalizer
        self.play(
            Create(finalize_block),
            GrowArrow(arrow_to_final_1),
            GrowArrow(arrow_to_final_2),
            GrowArrow(arrow_to_final_3)
        )

        self.wait(2)