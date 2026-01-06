from manim import *

# --- Custom Components ---

class ArchitectNode(VGroup):
    """Diagram එකේ තියෙන කොටු හදන්න ලේසි class එකක්"""
    def __init__(self, label, width=3, height=1.5, color=WHITE):
        super().__init__()
        self.box = Rectangle(width=width, height=height, color=color)
        self.text = Text(label, font_size=20, color=color).move_to(self.box.get_center())
        self.add(self.box, self.text)

class DataPacket(VGroup):
    """පද්ධතිය හරහා ගමන් කරන Data එක"""
    def __init__(self, icon_type="image", color=YELLOW):
        super().__init__()
        self.bg = Circle(radius=0.3, color=color, fill_opacity=0.5)
        
        # සරල සංකේත (Icons instead of loading real images for simplicity)
        if icon_type == "image":
            self.symbol = Square(side_length=0.3, color=WHITE) # Photo එකක් වගේ
        elif icon_type == "text":
            self.symbol = Text("T", font_size=24)
        elif icon_type == "voice":
            self.symbol = Text("V", font_size=24)
            
        self.symbol.move_to(self.bg.get_center())
        self.add(self.bg, self.symbol)

# --- Main Scene ---

class InputFlowScene(Scene):
    def construct(self):
        # 1. SETUP: Nodes ටික අඳිමු
        
        # වම් පැත්තේ Input Sources
        input_box = DashedVMobject(Rectangle(width=3, height=5, color=BLUE))
        input_label = Text("Input Channels\n(Img/Txt/Voice)", font_size=24, color=BLUE).move_to(input_box.get_center())
        input_box.to_edge(LEFT)
        
        # Normalization Layer (Image -> Text වෙන තැන)
        normalizer = ArchitectNode("Normalizer\n(OCR/Milvus/STT)", width=3.5, color=GREEN)
        normalizer.next_to(input_box, RIGHT, buff=1.5)
        
        # Guardrails
        guardrail = ArchitectNode("Guardrails\n(Safety/Jailbreak)", width=3, color=RED)
        guardrail.next_to(normalizer, RIGHT, buff=1.5)
        
        # Triage Agent
        triage = ArchitectNode("Triage Agent", width=2.5, color=WHITE)
        triage.next_to(guardrail, RIGHT, buff=1.5)

        # Arrows (Flow lines)
        arrow1 = Arrow(input_box.get_right(), normalizer.get_left(), buff=0.1)
        arrow2 = Arrow(normalizer.get_right(), guardrail.get_left(), buff=0.1)
        arrow3 = Arrow(guardrail.get_right(), triage.get_left(), buff=0.1)

        # Draw Diagram
        self.play(Create(input_box), Write(input_label))
        self.play(Create(normalizer), Create(guardrail), Create(triage))
        self.play(Create(arrow1), Create(arrow2), Create(arrow3))
        self.wait(1)

        # --- SCENARIO 4: Product Image Check ---
        
        # Step 1: Image එකක් එනවා (Input)
        packet = DataPacket(icon_type="image", color=YELLOW)
        packet.move_to(input_box.get_center())
        
        # Label එකක්: මොකක්ද මේ එවන්නේ?
        packet_label = Text("User: [Photo of Shoe]", font_size=18, color=YELLOW)
        packet_label.next_to(packet, UP)
        
        self.play(FadeIn(packet), Write(packet_label))
        self.wait(0.5)

        # Step 2: Normalizer එකට යනවා
        self.play(
            packet.animate.move_to(normalizer.get_center()),
            packet_label.animate.next_to(normalizer, UP),
            run_time=1.5
        )
        
        # Step 3: Transformation (Image -> Text)
        # මෙතනදි අපි පෙන්නනවා Milvus/Voting Algorithm එක වැඩ කරන බව
        processing_text = Text("Milvus Search...\nMatching SKU...", font_size=16, color=GREEN)
        processing_text.next_to(normalizer, DOWN)
        self.play(Write(processing_text))
        self.wait(1) # Processing time
        
        # Packet එක වෙනස් වෙනවා Text Packet එකක් බවට
        text_packet = DataPacket(icon_type="text", color=BLUE)
        text_packet.move_to(normalizer.get_center())
        
        # අලුත් Label එක (Converted Text)
        new_label = Text("Text: 'Check Stock: Red Shoe SKU-123'", font_size=16, color=BLUE)
        new_label.next_to(guardrail, UP) # ඊළඟ තැනට ලෑස්ති කරනවා

        self.play(
            Transform(packet, text_packet),
            Transform(packet_label, new_label),
            FadeOut(processing_text)
        )
        
        # Step 4: Guardrails Check
        self.play(
            packet.animate.move_to(guardrail.get_center()),
            packet_label.animate.next_to(guardrail, UP),
            run_time=1
        )
        
        # Check කරන බව පෙන්නන්න
        check_icon = Text("✅ Safe", font_size=20, color=GREEN).next_to(guardrail, DOWN)
        self.play(FadeIn(check_icon))
        self.wait(0.5)

        # Step 5: Triage එකට යැවීම
        self.play(
            packet.animate.move_to(triage.get_center()),
            packet_label.animate.next_to(triage, UP),
            FadeOut(check_icon),
            run_time=1
        )
        
        # Triage Decision (Thinking Bubble concept)
        thought_bubble = RoundedRectangle(corner_radius=0.5, height=1.5, width=4, color=YELLOW)
        thought_bubble.next_to(triage, DOWN)
        thought_text = Text("Intent: Stock Check\nRoute: Sales Agent", font_size=20)
        thought_text.move_to(thought_bubble.get_center())
        
        self.play(Create(thought_bubble), Write(thought_text))
        self.wait(2)