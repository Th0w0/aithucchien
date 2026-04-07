# Lab 4: AI Agent - TravelBuddy

## Mô tả dự án

Dự án này triển khai một AI Agent trợ lý du lịch tên TravelBuddy sử dụng LangGraph và Google Generative AI (Gemini). Agent có khả năng tư vấn du lịch Việt Nam, tìm chuyến bay, khách sạn và tính toán ngân sách dựa trên yêu cầu của người dùng.

## Cấu trúc dự án

- `agent.py`: File chính chứa logic của AI Agent, sử dụng LangGraph để quản lý trạng thái và luồng hội thoại.
- `tools.py`: Chứa các công cụ (tools) mô phỏng tìm kiếm chuyến bay, khách sạn và tính toán ngân sách.
- `system_prompt.txt`: Prompt hệ thống định nghĩa vai trò và quy tắc của agent.
- `requirements.txt`: Danh sách các thư viện Python cần thiết.
- `run_test.py`: Script để chạy các test case mẫu.
- `test_api.py`: Script test API.
- `test_results.md`: Kết quả test.

## Yêu cầu hệ thống

- Python 3.8+
- Google API Key (để sử dụng Gemini AI)
- Các thư viện trong `requirements.txt`

## Cài đặt

1. Clone hoặc tải dự án về máy.

2. Cài đặt các thư viện cần thiết:
   ```
   pip install -r requirements.txt
   ```

3. Tạo file `.env` trong thư mục gốc và thêm Google API Key:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## Chạy agent

Để chạy agent và test với các trường hợp mẫu:

```
python run_test.py
```

Agent sẽ xử lý các yêu cầu du lịch và trả lời bằng tiếng Việt.

## Cách sử dụng

Agent TravelBuddy hỗ trợ:
- Tìm chuyến bay giữa các thành phố Việt Nam
- Tìm khách sạn theo thành phố và ngân sách
- Tính toán ngân sách chuyến đi
- Tư vấn lịch trình du lịch

Ví dụ yêu cầu:
- "Tìm chuyến bay từ Hà Nội đến Đà Nẵng"
- "Tôi muốn đi Phú Quốc với ngân sách 5 triệu"
- "Gợi ý khách sạn ở Đà Nẵng dưới 1 triệu/đêm"

## Lưu ý

- Agent chỉ trả lời các câu hỏi liên quan đến du lịch. Các yêu cầu ngoài phạm vi sẽ bị từ chối.
- Dữ liệu chuyến bay và khách sạn là giả lập (mock data) cho mục đích demo.
- Đảm bảo có kết nối internet để gọi API Gemini.