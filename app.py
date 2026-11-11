
import streamlit as st
import pandas as pd
import joblib

# ==========================================
# 1. CẤU HÌNH GIAO DIỆN
# ==========================================

st.set_page_config(
    page_title="Dự đoán mức độ nghiện mạng xã hội",
    page_icon="📱",
    layout="wide"
)

# ==========================================
# 2. TẢI MÔ HÌNH
# ==========================================

bundle = joblib.load("/content/random_forest_bundle.pkl")

model = bundle["model"]
metadata = bundle["metadata"]

# ==========================================
# 3. TÊN CÁC TRƯỜNG BẰNG TIẾNG VIỆT
# ==========================================

display_names = {
    "Age": "Tuổi",
    "Gender": "Giới tính",
    "Occupation": "Nghề nghiệp",
    "Relationship_Status": "Tình trạng mối quan hệ",
    "Primary_Platform": "Nền tảng mạng xã hội sử dụng chính",
    "Daily_Usage_Hours": "Thời gian sử dụng mỗi ngày (giờ)",
    "Platforms_Used_Count": "Số nền tảng mạng xã hội sử dụng",
    "Posts_Per_Week": "Số bài đăng mỗi tuần",
    "Late_Night_Usage": "Có sử dụng mạng xã hội vào ban đêm không?",
    "First_Check_Morning": "Thời điểm kiểm tra mạng xã hội lần đầu vào buổi sáng",
    "Notifications_Per_Day": "Số thông báo nhận được mỗi ngày",
    "FOMO_Score": "Mức độ sợ bị bỏ lỡ thông tin",
    "Social_Comparison_Score": "Mức độ so sánh bản thân với người khác",
    "Validation_Seeking_Score": "Mức độ tìm kiếm sự công nhận",
    "Scroll_Without_Purpose": "Mức độ lướt mạng xã hội không có mục đích",
    "Tried_To_Cut_Back": "Đã từng cố gắng giảm thời gian sử dụng chưa?",
    "Failed_To_Cut_Back": "Đã từng thất bại khi cố gắng giảm sử dụng chưa?",
    "Anxiety_Score": "Mức độ lo âu",
    "Depression_Score": "Mức độ buồn bã và mất hứng thú",
    "Loneliness_Score": "Mức độ cảm thấy cô đơn",
    "Self_Esteem_Score": "Mức độ tự tin và đánh giá bản thân",
    "Sleep_Quality_Score": "Chất lượng giấc ngủ",
    "Sleep_Hours": "Số giờ ngủ mỗi ngày",
    "Productivity_Loss_Score": "Mức độ ảnh hưởng đến năng suất",
    "Offline_Relationship_Quality": "Chất lượng mối quan hệ ngoài đời",
    "Physical_Activity_Hrs_Week": "Thời gian hoạt động thể chất mỗi tuần (giờ)",
    "Screen_Free_Time_Hrs": "Thời gian không sử dụng thiết bị điện tử (giờ)",
    "Mental_Wellbeing_Score": "Mức độ sức khỏe tinh thần"
}

# ==========================================
# 4. CÂU HỎI TỰ ĐÁNH GIÁ
# ==========================================

score_questions = {
    "FOMO_Score": "Bạn sợ bỏ lỡ thông tin trên mạng xã hội ở mức độ nào?",
    "Social_Comparison_Score": "Bạn thường so sánh bản thân với người khác trên mạng xã hội ở mức độ nào?",
    "Validation_Seeking_Score": "Bạn quan tâm đến lượt thích và bình luận của người khác ở mức độ nào?",
    "Scroll_Without_Purpose": "Bạn thường lướt mạng xã hội không có mục đích ở mức độ nào?",
    "Anxiety_Score": "Bạn thường cảm thấy lo lắng ở mức độ nào?",
    "Depression_Score": "Bạn thường cảm thấy buồn bã hoặc mất hứng thú ở mức độ nào?",
    "Loneliness_Score": "Bạn thường cảm thấy cô đơn ở mức độ nào?",
    "Self_Esteem_Score": "Bạn đánh giá sự tự tin của bản thân ở mức độ nào?",
    "Sleep_Quality_Score": "Bạn đánh giá chất lượng giấc ngủ của mình như thế nào?",
    "Productivity_Loss_Score": "Mạng xã hội ảnh hưởng đến học tập hoặc công việc của bạn ở mức độ nào?",
    "Offline_Relationship_Quality": "Bạn đánh giá chất lượng các mối quan hệ ngoài đời như thế nào?",
    "Mental_Wellbeing_Score": "Bạn đánh giá sức khỏe tinh thần của mình như thế nào?"
}

# ==========================================
# 5. DỊCH KẾT QUẢ
# ==========================================

label_translation = {
    "Low": "Thấp",
    "Moderate": "Trung bình",
    "High": "Cao",
    "Severe": "Nghiêm trọng"
}

# ==========================================
# 6. CHIA NHÓM THÔNG TIN
# ==========================================

groups = {
    "👤 1. Thông tin cá nhân": [
        "Age", "Gender", "Occupation", "Relationship_Status"
    ],

    "📱 2. Thói quen sử dụng mạng xã hội": [
        "Primary_Platform",
        "Daily_Usage_Hours",
        "Platforms_Used_Count",
        "Posts_Per_Week",
        "Late_Night_Usage",
        "First_Check_Morning",
        "Notifications_Per_Day"
    ],

    "🧠 3. Hành vi và tâm lý": [
        "FOMO_Score",
        "Social_Comparison_Score",
        "Validation_Seeking_Score",
        "Scroll_Without_Purpose",
        "Tried_To_Cut_Back",
        "Failed_To_Cut_Back",
        "Anxiety_Score",
        "Depression_Score",
        "Loneliness_Score",
        "Self_Esteem_Score",
        "Mental_Wellbeing_Score"
    ],

    "🌙 4. Giấc ngủ và sức khỏe": [
        "Sleep_Quality_Score",
        "Sleep_Hours",
        "Physical_Activity_Hrs_Week",
        "Screen_Free_Time_Hrs"
    ],

    "📚 5. Học tập và các mối quan hệ": [
        "Productivity_Loss_Score",
        "Offline_Relationship_Quality"
    ]
}

integer_features = [
    "Age",
    "Platforms_Used_Count",
    "Posts_Per_Week",
    "Notifications_Per_Day"
]

# ==========================================
# 7. TIÊU ĐỀ
# ==========================================

st.title("📱 DỰ ĐOÁN MỨC ĐỘ NGHIỆN MẠNG XÃ HỘI")

st.write(
    "Hệ thống sử dụng mô hình Random Forest để dự đoán "
    "mức độ nghiện mạng xã hội dựa trên thông tin cá nhân, "
    "thói quen sử dụng và các yếu tố tâm lý."
)

st.info(
    "💡 Hãy trả lời các câu hỏi theo tình trạng thực tế của bạn. "
    "Với các câu hỏi đánh giá, hãy chọn mức điểm phù hợp."
)

# ==========================================
# 8. HÀM TẠO TRƯỜNG NHẬP LIỆU
# ==========================================

user_input = {}

def create_input(col):

    label = display_names.get(col, col)

    if col in metadata["numeric_features"]:

        default = metadata["defaults"][col]
        min_value, max_value = metadata["ranges"][col]

        min_value = float(min_value)
        max_value = float(max_value)

        if max_value <= min_value:
            max_value = min_value + 1

        default = min(max(float(default), min_value), max_value)

        # Câu hỏi tự đánh giá bằng thanh trượt
        if col in score_questions:

            st.markdown(f"**{score_questions[col]}**")

            if min_value.is_integer() and max_value.is_integer():

                user_input[col] = st.slider(
                    label,
                    min_value=int(min_value),
                    max_value=int(max_value),
                    value=int(default),
                    key=col
                )

            else:

                user_input[col] = st.slider(
                    label,
                    min_value=min_value,
                    max_value=max_value,
                    value=default,
                    step=0.1,
                    key=col
                )

        # Các trường số nguyên
        elif col in integer_features:

            # Số thông báo nhận được mỗi ngày
            if col == "Notifications_Per_Day":

                user_input[col] = st.number_input(
                    label,
                    min_value=int(min_value),
                    max_value=int(max_value),
                    value=int(default),
                    step=1,
                    key=col,
                    help=f"Giá trị hợp lệ theo dữ liệu huấn luyện: {int(min_value)} đến {int(max_value)}."
                )

            else:

                user_input[col] = st.number_input(
                    label,
                    min_value=int(min_value),
                    max_value=int(max_value),
                    value=int(default),
                    step=1,
                    key=col
                )

        # Các trường số thực
        else:

            user_input[col] = st.number_input(
                label,
                min_value=min_value,
                max_value=max_value,
                value=default,
                step=0.5,
                key=col
            )

    # Các trường phân loại
    elif col in metadata["categorical_features"]:

        categories = metadata["categories"][col]
        default = metadata["defaults"][col]

        default_index = (
            categories.index(default)
            if default in categories else 0
        )

        user_input[col] = st.selectbox(
            label,
            options=categories,
            index=default_index,
            key=col
        )

# ==========================================
# 9. GIAO DIỆN NHẬP THÔNG TIN
# ==========================================

with st.form("prediction_form"):

    feature_columns = metadata["feature_columns"]

    for group_name, features in groups.items():

        available_features = [
            col for col in features
            if col in feature_columns
        ]

        if available_features:

            st.subheader(group_name)

            left, right = st.columns(2)

            for index, col in enumerate(available_features):

                with (left if index % 2 == 0 else right):
                    create_input(col)

            st.divider()

    # Hiển thị những trường chưa được xếp nhóm
    remaining_features = [
        col for col in feature_columns
        if col not in user_input
    ]

    if remaining_features:

        st.subheader("Thông tin khác")

        left, right = st.columns(2)

        for index, col in enumerate(remaining_features):

            with (left if index % 2 == 0 else right):
                create_input(col)

    submitted = st.form_submit_button(
        "🔍 DỰ ĐOÁN MỨC ĐỘ NGHIỆN",
        use_container_width=True
    )

# ==========================================
# 10. DỰ ĐOÁN VÀ HIỂN THỊ KẾT QUẢ
# ==========================================

if submitted:

    input_df = pd.DataFrame(
        [user_input],
        columns=feature_columns
    )

    prediction = model.predict(input_df)[0]

    predicted_label = label_translation.get(
        str(prediction), str(prediction)
    )

    st.divider()

    st.subheader("📊 KẾT QUẢ DỰ ĐOÁN")

    st.success(
        f"Mức độ nghiện mạng xã hội dự đoán: {predicted_label}"
    )

    # Xác suất dự đoán
    probabilities = model.predict_proba(input_df)[0]
    classes = model.classes_

    probability_df = pd.DataFrame({
        "Mức độ nghiện": [
            label_translation.get(str(c), str(c))
            for c in classes
        ],
        "Xác suất (%)": probabilities * 100
    })

    st.write("Xác suất dự đoán của từng mức độ:")

    st.bar_chart(
        probability_df.set_index("Mức độ nghiện")
    )

    st.dataframe(
        probability_df.style.format({
            "Xác suất (%)": "{:.2f}%"
        }),
        use_container_width=True,
        hide_index=True
    )

    st.warning(
        "Lưu ý: Kết quả chỉ mang tính tham khảo, "
        "không phải công cụ chẩn đoán sức khỏe tâm thần."
    )
