"""程序说明"""
# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
import jiagu
import pprint
import kivy.app
import kivy.uix.button
import kivy.uix.label
import kivy.uix.textinput
import kivy.uix.boxlayout

class NlpApp(kivy.app.App):



    def nlp_jiagu(self,btn):

        text =str(self.lbl.text.strip()).replace("\n","")
        if text[-2:] == "qg":
            sentiment = jiagu.sentiment(text[:-2])
            self.lbl.text =pprint.pformat(sentiment)
        elif text[-2:] == "cq":
            keywords = jiagu.keywords(text, 5)  # 关键词
            self.lbl.text = pprint.pformat(keywords)
        elif text[-2:] == "jl":
            if "," in self.lbl.text:

                docs = self.lbl.text.split(",")
            else:
                docs = self.lbl.text.split("，")
            #print(docs)
            cluster = jiagu.text_cluster(docs)
            self.lbl.text = pprint.pformat(cluster)


        else:
            knowledge = jiagu.knowledge(text)
            self.lbl.text =pprint.pformat(knowledge)

    def build(self):
        layout = kivy.uix.boxlayout.BoxLayout(orientation="vertical",)
        self.lbl = kivy.uix.textinput.TextInput(text='姚明1980年9月12日出生于上海市徐汇区，祖籍江苏省苏州市吴江区震泽镇，前中国职业篮球运动员，司职中锋，现任中职联公司董事长兼总经理。',
                                                font_name="arialuni.ttf",size_hint=(1, 7))

        btn = kivy.uix.button.Button(text="开始",font_name="arialuni.ttf",size_hint=(1, 3))
        btn.bind(on_press=self.nlp_jiagu)


        layout.add_widget(self.lbl)
        layout.add_widget(btn)
        return layout


NlpApp().run()