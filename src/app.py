# -*- coding: utf-8 -*-
"""Webアプリのサンプルです"""

# ライブラリのインポート
from datetime import datetime, timedelta

from flask import Flask, render_template, request
from markupsafe import Markup

import omikuji
import school_timetable
import weather_forecast

# Flaskのインスタンス化
application = Flask(__name__, static_folder="static", template_folder="templates")


@application.route("/")
@application.route("/index")
def index() -> str:
    """トップページ

    Returns:
        str: レンダリング結果
    """
    return render_template("./index.html")


@application.route("/dashboard", methods=["GET", "POST"])
def tomorrow_plan() -> str:
    exercises = [
        {'date': '2024-12-21', 'type': 'ランニング', 'duration': 30},
        {'date': '2024-12-22', 'type': 'ウォーキング', 'duration': 45}
    ]
    meals = [
        {'date': '2024-12-21', 'name': '朝食', 'calories': 300},
        {'date': '2024-12-21', 'name': '昼食', 'calories': 500}
    ]
    bmi = 22.5
    bmi_message = '正常体重です'
    advice = '定期的な運動を続けましょう！'

    return render_template(
        './dashboard.html',
        exercises=exercises,
        meals=meals,
        bmi=bmi,
        bmi_message=bmi_message,
        advice=advice
    )

@application.route("/add", methods=["GET", "POST"])
def add_record() -> str:
    """記録を追加するページ

    Returns:
        str: レンダリング結果
    """
    if request.method == "POST":
        # フォームデータを取得
        record_type = request.form.get("record_type")  # 運動か食事か
        date = request.form.get("date")
        if record_type == "exercise":
            exercise_type = request.form.get("type")
            duration = request.form.get("duration")
            # ここでデータを保存する処理を追加（データベースやファイルなど）
            print(f"運動記録追加: {date}, {exercise_type}, {duration}分")
        elif record_type == "meal":
            meal_name = request.form.get("name")
            calories = request.form.get("calories")
            # ここでデータを保存する処理を追加（データベースやファイルなど）
            print(f"食事記録追加: {date}, {meal_name}, {calories}kcal")

    return render_template('./add.html')