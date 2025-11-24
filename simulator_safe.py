import math
import streamlit as st

st.title("ガチャ確率シミュレーター（安全版）")

x = st.number_input("全体の種類数 (例: 10)", min_value=1)
y = st.number_input("欲しい種類数 (例: 2)", min_value=1, max_value=int(x))
z = st.number_input("目標確率 (%) (例: 90)", min_value=1.0, max_value=100.0)

if st.button("計算開始"):
    try:
        if x >= y:
            p_none = (x - y) / x

            # 計算可能かチェック
            if p_none <= 0:
                st.error("欲しいものの数が全体と同じか多すぎます。計算できません。")
            elif (1 - z/100) <= 0:
                st.error("目標確率が100%です。計算できません。")
            else:
                n = math.log(1 - z/100) / math.log(p_none)
                st.success(f"必要な回数: {math.ceil(n)} 回")
        else:
            st.error("欲しい種類数 y は全体の種類数 x 以下にしてください。")
    except Exception:
        st.error("計算中にエラーが発生しました。入力値を確認してください。")

