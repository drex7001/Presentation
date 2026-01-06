from manim import *
from manim_slides import Slide

class EcommerceFinal(Slide, MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        # --- TITLE ---
        title = Text("Multi-Agent AI CRM Architecture", font_size=40, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        self.next_slide()

        self.play(title.animate.to_edge(UP))

        # --- SECTION 1: INPUTS ---
        input_box = Rectangle(height=3, width=4.5, color=GREY)
        input_title = Text("Channels & Inputs", font_size=24).next_to(input_box, UP, buff=0.1)
        
        # දත්ත ඇතුළත් කිරීම (Notes: FB, WA, TikTok, YouTube, Email)
        # දැන් අපිට කෙලින්ම BulletedList භාවිතා කළ හැකියි!
        channels_list = BulletedList(
            "WhatsApp, Facebook", 
            "TikTok, YouTube", 
            "Email", 
            "Voice/Video/PDF",
            font_size=22, 
            dot_color=WHITE
        )
        channels_list.move_to(input_box.get_center())

        inputs_group = VGroup(input_box, input_title, channels_list).scale(0.8).to_edge(LEFT, buff=0.5)
        self.play(Create(input_box), Write(input_title), FadeIn(channels_list))
        self.wait(0.5)

        # --- SECTION 2: ORCHESTRATOR ---
        # Notes: Triage & FAQ
        triage_box = RoundedRectangle(corner_radius=0.2, height=1.5, width=2.5, color=YELLOW)
        triage_text = Text("Orchestrator\n(Triage)", font_size=20, color=YELLOW).move_to(triage_box.get_center())
        
        triage_group = VGroup(triage_box, triage_text).shift(LEFT * 0.5)
        arrow_in = Arrow(inputs_group.get_right(), triage_group.get_left(), buff=0.1)

        self.play(Create(triage_group), GrowArrow(arrow_in))
        self.wait(0.5)

        # --- SECTION 3: AGENTS ---
        sales_agent = VGroup(RoundedRectangle(height=1.2, width=3.5, color=GREEN), Text("Sales (Pre-sale)", font_size=24))
        ops_agent = VGroup(RoundedRectangle(height=1.2, width=3.5, color=ORANGE), Text("Ops (Alterations)", font_size=24))
        supp_agent = VGroup(RoundedRectangle(height=1.2, width=3.5, color=PURPLE), Text("Support (After-sale)", font_size=24))

        for grp in [sales_agent, ops_agent, supp_agent]:
            grp[1].move_to(grp[0].get_center())

        agents_group = VGroup(sales_agent, ops_agent, supp_agent).arrange(DOWN, buff=2.5).to_edge(RIGHT, buff=1)
        arrows_out = VGroup(*[Arrow(triage_group.get_right(), agent.get_left(), buff=0.1) for agent in agents_group])

        self.play(Create(agents_group), Create(arrows_out))
        self.next_slide()

        # --- ZOOM & REVEAL (LaTeX Lists) ---
        
        # 1. Sales Agent
        self.play(self.camera.frame.animate.scale(0.6).move_to(sales_agent), run_time=1.5)
        
        # Notes: Sales Tools
        sales_tools = BulletedList(
            "Search (Product/Image)", 
            "Check Inventory", 
            "Payment Info",
            font_size=22, dot_color=GREEN
        ).next_to(sales_agent, DOWN, buff=0.2)
        
        self.play(Write(sales_tools))
        self.next_slide()

        # 2. Ops Agent
        self.play(self.camera.frame.animate.move_to(ops_agent), FadeOut(sales_tools), run_time=1.5)
        
        # Notes: Ops Tools
        ops_tools = BulletedList(
            "Place/Cancel Order", 
            "Add/Remove Item", 
            "Address Change",
            font_size=22, dot_color=ORANGE
        ).next_to(ops_agent, DOWN, buff=0.2)
        
        self.play(Write(ops_tools))
        self.next_slide()

        # 3. Support Agent
        self.play(self.camera.frame.animate.move_to(supp_agent), FadeOut(ops_tools), run_time=1.5)
        
        # Notes: Support Tools
        supp_tools = BulletedList(
            "Returns & Exchanges", 
            "Refund Status", 
            "KB Search",
            font_size=22, dot_color=PURPLE
        ).next_to(supp_agent, DOWN, buff=0.2)
        
        self.play(Write(supp_tools))
        self.next_slide()

        # --- FINALIZE ---
        self.play(FadeOut(supp_tools), Restore(self.camera.frame), run_time=2)
        finalize = Text("Finalize Agent Response", font_size=24, color=RED).to_edge(DOWN, buff=0.5)
        self.play(Write(finalize))
        self.next_slide()
        self.wait(1)