
================================================================================
TEST CASE 1
USER: 'Hello'
2026-04-07 18:19:24,247 | INFO | travelbuddy | Invoking LLM with 2 message(s)
2026-04-07 18:19:25,872 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:19:25,874 | INFO | travelbuddy | Direct response returned
TravelBuddy:
Chào bạn, mình là TravelBuddy đây! Mình có thể giúp gì cho chuyến đi sắp tới của bạn? Bạn đang muốn tìm chuyến bay, khách sạn hay lên kế hoạch du lịch ở đâu không?

================================================================================
TEST CASE 2
USER: 'Xin chào, tôi muốn đi du lịch nhưng chưa biết đi đâu'
2026-04-07 18:19:25,875 | INFO | travelbuddy | Invoking LLM with 2 message(s)
2026-04-07 18:19:27,758 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:19:27,759 | INFO | travelbuddy | Direct response returned
TravelBuddy:
Chào bạn, rất vui được hỗ trợ! Để mình gợi ý cho bạn những điểm đến phù hợp, bạn có thể cho mình biết thêm về:

1.  **Sở thích của bạn là gì?** (Ví dụ: thích biển, núi, khám phá văn hóa, ẩm thực, hay nghỉ dưỡng sang chảnh?)
2.  **Bạn dự định đi trong bao lâu?**
3.  **Ngân sách khoảng bao nhiêu?**
4.  **Bạn muốn đi cùng ai?** (Gia đình, bạn bè, hay đi một mình?)

Càng nhiều thông tin, mình càng dễ dàng tìm được nơi ưng ý cho bạn đó!

================================================================================
TEST CASE 3
USER: 'Tìm giúp tôi chuyến bay từ Hà Nội đến Đà Nẵng'
2026-04-07 18:19:27,761 | INFO | travelbuddy | Invoking LLM with 2 message(s)
2026-04-07 18:19:30,020 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:19:30,022 | INFO | travelbuddy | Tool called: search_flights | args={'destination': 'Đà Nẵng', 'origin': 'Hà Nội'}
2026-04-07 18:19:30,025 | INFO | travelbuddy | Invoking LLM with 4 message(s)
2026-04-07 18:19:32,131 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:19:32,131 | INFO | travelbuddy | Direct response returned
TravelBuddy:
Tuyệt vời! Có một vài lựa chọn cho bạn đây:

*   **VietJet Air:** 08:30 - 09:50, giá 890.000đ (hạng economy)
*   **Bamboo Airways:** 11:00 - 12:20, giá 1.200.000đ (hạng economy)
*   **Vietnam Airlines:** 06:00 - 07:20, giá 1.450.000đ (hạng economy)
*   **Vietnam Airlines:** 14:00 - 15:20, giá 2.800.000đ (hạng business)

Bạn thấy chuyến nào phù hợp với mình không? Hay bạn muốn mình tìm thêm khách sạn ở Đà Nẵng luôn không?

================================================================================
TEST CASE 4
USER: 'Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp tôi!'
2026-04-07 18:19:32,137 | INFO | travelbuddy | Invoking LLM with 2 message(s)
2026-04-07 18:19:34,094 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:19:34,096 | INFO | travelbuddy | Tool called: search_flights | args={'origin': 'Hà Nội', 'destination': 'Phú Quốc'}
2026-04-07 18:19:34,098 | INFO | travelbuddy | Invoking LLM with 4 message(s)
2026-04-07 18:19:37,000 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:19:37,001 | INFO | travelbuddy | Tool called: calculate_budget | args={'expenses': 'vé_máy_bay:1100000', 'total_budget': 5000000}
2026-04-07 18:19:37,003 | INFO | travelbuddy | Invoking LLM with 6 message(s)
2026-04-07 18:19:38,259 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:19:38,262 | INFO | travelbuddy | Tool called: search_hotels | args={'max_price_per_night': 1950000, 'city': 'Phú Quốc', 'sort_by': 'rating'}
2026-04-07 18:19:38,262 | INFO | travelbuddy | Invoking LLM with 8 message(s)
2026-04-07 18:19:40,907 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:19:40,907 | INFO | travelbuddy | Direct response returned
TravelBuddy:
Chào bạn, với ngân sách 5 triệu cho chuyến đi Phú Quốc 2 đêm từ Hà Nội, mình đã tìm được vài lựa chọn đây:

**Chuyến bay:**
*   VietJet Air | 16:00 - 18:15 | 1.100.000đ | economy (Đây là chuyến rẻ nhất nha)

**Ngân sách:**
*   Tổng chi cho vé máy bay: 1.100.000đ
*   Ngân sách còn lại: 3.900.000đ (cho 2 đêm ở Phú Quốc)

**Khách sạn ở Phú Quốc (với ngân sách còn lại, khoảng 1.950.000đ/đêm):**
*   Sol by Meliá | 4⭐ | 1.500.000đ/đêm | Bãi Trường | rating 4.2 (Khá ổn áp đó bạn, có hồ bơi đẹp)
*   Lahana Resort | 3⭐ | 800.000đ/đêm | Dương Đông | rating 4.0 (Nếu muốn tiết kiệm hơn mà vẫn chất lượng)
*   9Station Hostel | 2⭐ | 200.000đ/đêm | Dương Đông | rating 4.5 (Nếu bạn thích trải nghiệm hostel, giá cực tốt)

Bạn thấy sao về những gợi ý này? Có muốn mình tìm thêm thông tin gì không?

================================================================================
TEST CASE 5
USER: 'Tôi muốn đặt khách sạn'
2026-04-07 18:19:40,917 | INFO | travelbuddy | Invoking LLM with 2 message(s)
2026-04-07 18:19:42,211 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:19:42,211 | INFO | travelbuddy | Direct response returned
TravelBuddy:
Tuyệt vời! Bạn muốn đặt khách sạn ở thành phố nào và ngân sách của bạn cho mỗi đêm là bao nhiêu?

================================================================================
TEST CASE 6
USER: 'Giải giúp tôi bài tập linked list'
2026-04-07 18:19:42,211 | INFO | travelbuddy | Invoking LLM with 2 message(s)
2026-04-07 18:19:44,115 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:19:44,117 | INFO | travelbuddy | Direct response returned
TravelBuddy:
Chào bạn, mình là trợ lý du lịch của TravelBuddy. Mình rất sẵn lòng giúp bạn lên kế hoạch cho những chuyến đi thú vị ở Việt Nam. Tuy nhiên, mình không thể giúp bạn giải bài tập về linked list được. Mình chỉ hỗ trợ các vấn đề liên quan đến du lịch thôi.    

Bạn có muốn mình giúp tìm chuyến bay, khách sạn, hay gợi ý lịch trình cho chuyến đi sắp tới không?

================================================================================
TEST CASE 7
USER: 'Cho tôi tìm chuyến bay từ Hà Nội đến Cần Thơ'
2026-04-07 18:19:44,119 | INFO | travelbuddy | Invoking LLM with 2 message(s)
2026-04-07 18:19:45,679 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:19:45,681 | INFO | travelbuddy | Tool called: search_flights | args={'origin': 'Hà Nội', 'destination': 'Cần Thơ'}
2026-04-07 18:19:45,683 | INFO | travelbuddy | Invoking LLM with 4 message(s)
2026-04-07 18:19:47,142 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:19:47,142 | INFO | travelbuddy | Direct response returned
TravelBuddy:
Ôi, tiếc quá! Hiện tại mình không tìm thấy chuyến bay thẳng nào từ Hà Nội đến Cần Thơ. Bạn có muốn mình tìm chuyến bay đến một thành phố khác gần Cần Thơ không, hoặc bạn muốn thử tìm lại vào một thời điểm khác?

================================================================================
TEST CASE 8
USER: 'Không tìm thấy khách sạn tại Đà Nẵng với giá dưới 100,000đ.'
2026-04-07 18:19:47,142 | INFO | travelbuddy | Invoking LLM with 2 message(s)
2026-04-07 18:19:49,060 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:19:49,062 | INFO | travelbuddy | Direct response returned
TravelBuddy:
Đúng là tìm khách sạn dưới 100.000đ ở Đà Nẵng hơi khó đó bạn. Bạn có muốn mình tìm khách sạn với mức giá cao hơn một chút không, hoặc bạn có ngân sách cụ thể nào cho khách sạn không?

================================================================================
Done.