import streamlit as st


st.set_page_config(page_title='Thông tin bạn thân', page_icon=':friends:', layout='wide')
st.title('Lưu thông tin những người bạn thân')

friends_info = {
      'Nguyễn Văn A': {'Tuổi': 12, 'Sở thích': 'Chơi thể thao', 'Nghề nghiệp': 'Học sinh'},
      'Trần Thị B': {'Tuổi': 11, 'Sở thích': 'Đọc sách', 'Nghề nghiệp': 'Học sinh'},
      'Lê Văn C': {'Tuổi': 10, 'Sở thích': 'Du lịch', 'Nghề nghiệp': 'Học sinh'},
      'Phạm Thị D': {'Tuổi': 9, 'Sở thích': 'Nấu ăn', 'Nghề nghiệp': 'Học sinh'},
  }

selected_friend = st.selectbox('Chọn tên bạn của bạn:', list(friends_info.keys()))

if selected_friend:
      st.subheader(f'Thông tin về {selected_friend}:')
      st.write(f"**Tuổi:** {friends_info[selected_friend]['Tuổi']}")
      st.write(f"**Sở thích:** {friends_info[selected_friend]['Sở thích']}")
      st.write(f"**Nghề nghiệp:** {friends_info[selected_friend]['Nghề nghiệp']}")