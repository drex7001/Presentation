from manim import *


class EcommerceFullScene(MovingCameraScene):
    def create_custom_list(self, items, color):
        rows = []
        for item in items:
            dot = Dot(radius=0.06, color=color)
            text = Text(item, font_size=24, color=color)
            dot.next_to(text, LEFT, buff=0.25)
            dot.set_y(text.get_y())
            rows.append(VGroup(dot, text))
        return VGroup(*rows).arrange(DOWN, aligned_edge=LEFT, buff=0.28)

    def construct(self):
        self.camera.background_color = "#0b0f14"
        self.camera.frame.save_state()

        title = Text(
            "Multi-Agent AI Architecture for E-commerce CRM",
            font_size=46,
            color=WHITE,
        ).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.wait(0.4)

        # Inputs layer
        input_box = RoundedRectangle(
            corner_radius=0.2,
            height=5.0,
            width=4.8,
            color=BLUE_C,
        ).set_fill(BLUE_E, opacity=0.12)
        input_title = Text("Inputs Layer", font_size=28, color=BLUE_C).next_to(
            input_box, UP, buff=0.2
        )
        channels_label = Text("Channels", font_size=24, color=WHITE).next_to(
            input_box.get_top(), DOWN, buff=0.3
        )
        channels_list = self.create_custom_list(
            ["WhatsApp", "Facebook", "TikTok", "YouTube", "Email"],
            color=BLUE_C,
        ).next_to(channels_label, DOWN, aligned_edge=LEFT, buff=0.2)
        media_label = Text("Media Types", font_size=24, color=WHITE).next_to(
            channels_list, DOWN, aligned_edge=LEFT, buff=0.35
        )
        media_list = self.create_custom_list(
            ["Text", "Voice", "Image", "Video", "PDF Files"],
            color=BLUE_C,
        ).next_to(media_label, DOWN, aligned_edge=LEFT, buff=0.2)
        inputs_group = VGroup(
            input_box,
            input_title,
            channels_label,
            channels_list,
            media_label,
            media_list,
        ).to_edge(LEFT, buff=0.6)

        # Orchestrator layer
        triage_box = RoundedRectangle(
            corner_radius=0.25,
            height=2.2,
            width=4.0,
            color=TEAL_C,
        ).set_fill(TEAL_E, opacity=0.15)
        triage_title = Text("Orchestrator", font_size=28, color=TEAL_B)
        triage_detail = Text(
            "Triage: Greetings, FAQs, Routing",
            font_size=22,
            color=WHITE,
        )
        triage_text = VGroup(triage_title, triage_detail).arrange(DOWN, buff=0.2)
        triage_text.move_to(triage_box.get_center())
        triage_group = VGroup(triage_box, triage_text).next_to(
            inputs_group, RIGHT, buff=1.4
        )

        arrow_inputs = Arrow(
            inputs_group.get_right(),
            triage_group.get_left(),
            buff=0.15,
            color=GREY_B,
        )

        # Specialized agents layer
        def build_agent(label, color):
            box = RoundedRectangle(
                corner_radius=0.2,
                height=1.1,
                width=4.6,
                color=color,
            ).set_fill(color, opacity=0.18)
            text = Text(label, font_size=28, color=color).move_to(box.get_center())
            return VGroup(box, text)

        sales_agent = build_agent("Sales Agent", GREEN_C)
        ops_agent = build_agent("Ops Agent", ORANGE)
        support_agent = build_agent("Support Agent", PURPLE_C)

        agents_group = VGroup(sales_agent, ops_agent, support_agent).arrange(
            DOWN, buff=1.8
        ).to_edge(RIGHT, buff=0.6)

        arrows_to_agents = VGroup(
            Arrow(triage_group.get_right(), sales_agent.get_left(), buff=0.15, color=GREY_B),
            Arrow(triage_group.get_right(), ops_agent.get_left(), buff=0.15, color=GREY_B),
            Arrow(triage_group.get_right(), support_agent.get_left(), buff=0.15, color=GREY_B),
        )

        # Align the main layout lower to make space for the title.
        layout_shift = DOWN * 0.2
        inputs_group.shift(layout_shift)
        triage_group.shift(layout_shift)
        agents_group.shift(layout_shift)
        arrows_to_agents.shift(layout_shift)
        arrow_inputs.shift(layout_shift)

        # Overview: show Inputs -> Triage -> Agents
        self.play(
            Create(input_box),
            FadeIn(input_title),
            FadeIn(channels_label),
            FadeIn(channels_list),
            FadeIn(media_label),
            FadeIn(media_list),
            run_time=1.5,
        )
        self.play(
            Create(triage_box),
            FadeIn(triage_text),
            GrowArrow(arrow_inputs),
            run_time=1.2,
        )
        self.play(
            FadeIn(agents_group),
            LaggedStartMap(GrowArrow, arrows_to_agents, lag_ratio=0.15),
            run_time=1.4,
        )
        self.wait(1.0)

        # Step 1: Zoom to Sales Agent
        self.play(
            self.camera.frame.animate.scale(0.55).move_to(sales_agent),
            run_time=1.5,
        )
        sales_tools = self.create_custom_list(
            ["Search (Product/Image)", "Check Inventory", "Payment Info"],
            color=GREEN_C,
        ).next_to(sales_agent, RIGHT, buff=0.6)
        self.play(
            LaggedStartMap(FadeIn, sales_tools, shift=RIGHT * 0.2, lag_ratio=0.2)
        )
        self.wait(1.5)
        self.play(FadeOut(sales_tools), run_time=0.6)

        # Step 2: Pan to Ops Agent
        self.play(self.camera.frame.animate.move_to(ops_agent), run_time=1.4)
        ops_tools = self.create_custom_list(
            ["Place/Cancel Order", "Add/Remove Item", "Address Change"],
            color=ORANGE,
        ).next_to(ops_agent, RIGHT, buff=0.6)
        self.play(LaggedStartMap(FadeIn, ops_tools, shift=RIGHT * 0.2, lag_ratio=0.2))
        self.wait(1.5)
        self.play(FadeOut(ops_tools), run_time=0.6)

        # Step 3: Pan to Support Agent
        self.play(self.camera.frame.animate.move_to(support_agent), run_time=1.4)
        support_tools = self.create_custom_list(
            ["Returns & Exchanges", "Refund Status", "KB-Search"],
            color=PURPLE_C,
        ).next_to(support_agent, RIGHT, buff=0.6)
        self.play(
            LaggedStartMap(FadeIn, support_tools, shift=RIGHT * 0.2, lag_ratio=0.2)
        )
        self.wait(1.5)
        self.play(FadeOut(support_tools), run_time=0.6)

        # Restore full view and finalize
        self.play(Restore(self.camera.frame), run_time=2)

        finalize_box = RoundedRectangle(
            corner_radius=0.2,
            height=1.3,
            width=4.8,
            color=RED_C,
        ).set_fill(RED_E, opacity=0.2)
        finalize_title = Text("Finalize Agent", font_size=28, color=RED_C)
        finalize_detail = Text("Collates info and responds", font_size=22, color=WHITE)
        finalize_text = VGroup(finalize_title, finalize_detail).arrange(DOWN, buff=0.15)
        finalize_text.move_to(finalize_box.get_center())
        finalize_group = VGroup(finalize_box, finalize_text).move_to(
            DOWN * 3.2
        )

        finalize_arrow = Arrow(
            agents_group.get_bottom(),
            finalize_group.get_top(),
            buff=0.2,
            color=GREY_B,
        )

        self.play(FadeIn(finalize_group), GrowArrow(finalize_arrow))
        self.wait(2.5)
