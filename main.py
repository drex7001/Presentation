from manim import *

class EcommerceAI(Scene):
    def construct(self):
        # 1. Title
        title = Text("Multi-Agent AI CRM Architecture", font_size=32, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # 2. Input & Processing Layers (Notes: WA, FB, TikTok, YouTube, Email)
        input_box = Rectangle(height=2, width=3.5, color=GREY)
        input_label = Text("Channels: WA, FB,\nTikTok, YT, Email", font_size=16).next_to(input_box, UP, buff=0.1)
        media = Text("Text, Voice, Image,\nVideo, Files (PDF)", font_size=14, color=GREY_A).move_to(input_box.get_center())
        
        inputs = VGroup(input_box, input_label, media).scale(0.8).to_edge(LEFT, buff=0.4)
        self.play(Create(input_box), Write(input_label), FadeIn(media))

        # 3. Triage / Orchestrator Node (Notes: Handles greetings & FAQ)
        triage = VGroup(
            RoundedRectangle(corner_radius=0.1, height=1, width=2, color=YELLOW),
            Text("Orchestrator\n(Triage)", font_size=18, color=YELLOW)
        ).move_to(LEFT * 0.5)
        
        self.play(Create(triage[0]), Write(triage[1]), GrowArrow(Arrow(inputs.get_right(), triage.get_left())))

        # 4. Specialized Agents (The Three Main Sections)
        agents = VGroup(
            VGroup(RoundedRectangle(height=0.8, width=2.5, color=GREEN), Text("Sales (Pre-sale)", font_size=16)),
            VGroup(RoundedRectangle(height=0.8, width=2.5, color=ORANGE), Text("Ops (Alterations)", font_size=16)),
            VGroup(RoundedRectangle(height=0.8, width=2.5, color=PURPLE), Text("Support (After-sale)", font_size=16))
        ).arrange(DOWN, buff=0.6).to_edge(RIGHT, buff=0.5)

        for a in agents: a[1].move_to(a[0].get_center())
        arrows = VGroup(*[Arrow(triage.get_right(), a.get_left(), buff=0.1) for a in agents])
        self.play(Create(agents), Create(arrows))

        # 5. Adding Detailed Tools from your handwritten notes
        # Sales Tools: Search by image, check inventory, delivery info
        sales_tools = VGroup(
            Text("- Search (Product/Image)", font_size=12),
            Text("- Check Inventory", font_size=12),
            Text("- Payment & Delivery Info", font_size=12)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(agents[0], DOWN, buff=0.1).set_color(GREEN)

        # Ops Tools: Place/Cancel/Track Order, Add/Remove/Replace item, Address change
        ops_tools = VGroup(
            Text("- Place/Cancel/Track Order", font_size=12),
            Text("- Add/Remove/Replace Item", font_size=12),
            Text("- Address Change", font_size=12)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(agents[1], DOWN, buff=0.1).set_color(ORANGE)

        # Support Tools: Return/Exchange, Damage, Refund status, KB-search
        supp_tools = VGroup(
            Text("- Returns & Exchanges", font_size=12),
            Text("- Damage Items / Refunds", font_size=12),
            Text("- KB-Search", font_size=12)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(agents[2], DOWN, buff=0.1).set_color(PURPLE)

        # 6. Reveal Tools
        self.play(Write(sales_tools), Write(ops_tools), Write(supp_tools))
        self.wait(2)

        # 7. Finalize Agent (Final layer)
        finalize = Text("Finalize Agent Response", font_size=20, color=RED).to_edge(DOWN, buff=0.3)
        self.play(Write(finalize))
        self.wait(2)