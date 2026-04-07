
================================================================================
TEST CASE 1
USER: 'Hello'
2026-04-07 18:01:08,791 | INFO | travelbuddy | Invoking LLM with 2 message(s)
2026-04-07 18:01:10,337 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:01:10,339 | INFO | travelbuddy | Direct response returned
TravelBuddy:
Chào bạn, mình là TravelBuddy đây! Mình có thể giúp gì cho chuyến đi sắp tới của bạn? Bạn đang muốn tìm chuyến bay, khách sạn hay lên kế hoạch du lịch ở đâu không?

================================================================================
TEST CASE 2
USER: 'Xin chào, tôi muốn đi du lịch nhưng chưa biết đi đâu'
2026-04-07 18:01:10,341 | INFO | travelbuddy | Invoking LLM with 2 message(s)
2026-04-07 18:01:12,527 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:01:12,530 | INFO | travelbuddy | Direct response returned
TravelBuddy:
Chào bạn! Việt Nam mình có nhiều điểm đến đẹp lắm. Để mình gợi ý cho bạn vài chỗ nhé, bạn thích kiểu du lịch như thế nào?

*   **Thích biển đảo, nghỉ dưỡng?** Nha Trang, Đà Nẵng, Phú Quốc là những lựa chọn tuyệt vời.
*   **Thích khám phá văn hóa, lịch sử?** Huế, Hội An, Hà Nội sẽ rất phù hợp.
*   **Thích núi non hùng vĩ, trải nghiệm thiên nhiên?** Sapa, Hà Giang, Đà Lạt là những điểm đến không thể bỏ qua.

Bạn có thể cho mình biết thêm về:

*   **Ngân sách dự kiến** của bạn là khoảng bao nhiêu?
*   Bạn muốn đi trong **bao lâu**?
*   Bạn đi **một mình, với gia đình hay bạn bè**?

Càng nhiều thông tin, mình càng dễ gợi ý đúng ý bạn hơn đó!

================================================================================
TEST CASE 3
USER: 'Tìm giúp tôi chuyến bay từ Hà Nội đến Đà Nẵng'
2026-04-07 18:01:12,531 | INFO | travelbuddy | Invoking LLM with 2 message(s)
2026-04-07 18:01:14,218 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:01:14,220 | INFO | travelbuddy | Tool called: search_flights | args={'destination': 'Đà Nẵng', 'origin': 'Hà Nội'}
2026-04-07 18:01:14,223 | INFO | travelbuddy | Invoking LLM with 4 message(s)
2026-04-07 18:01:16,299 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:01:16,301 | INFO | travelbuddy | Direct response returned
TravelBuddy:
Tuyệt vời! Đây là một vài lựa chọn chuyến bay từ Hà Nội đi Đà Nẵng bạn có thể tham khảo:

*   **VietJet Air:** 08:30 - 09:50, giá 890.000đ (hạng economy)
*   **Bamboo Airways:** 11:00 - 12:20, giá 1.200.000đ (hạng economy)
*   **Vietnam Airlines:** 06:00 - 07:20, giá 1.450.000đ (hạng economy)

Bạn thấy chuyến nào phù hợp với mình không? Hay bạn muốn mình tìm thêm khách sạn ở Đà Nẵng luôn không?

================================================================================
TEST CASE 4
USER: 'Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp tôi!'
2026-04-07 18:01:16,304 | INFO | travelbuddy | Invoking LLM with 2 message(s)
2026-04-07 18:01:17,612 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:01:17,619 | INFO | travelbuddy | Tool called: search_flights | args={'destination': 'Phú Quốc', 'origin': 'Hà Nội'}
2026-04-07 18:01:17,622 | INFO | travelbuddy | Invoking LLM with 4 message(s)
2026-04-07 18:01:19,035 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:01:19,036 | INFO | travelbuddy | Tool called: calculate_budget | args={'expenses': 'vé_máy_bay:1100000', 'total_budget': 5000000}
2026-04-07 18:01:19,039 | INFO | travelbuddy | Invoking LLM with 6 message(s)
2026-04-07 18:01:20,852 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:01:20,852 | INFO | travelbuddy | Tool called: search_hotels | args={'sort_by': 'rating', 'max_price_per_night': 1950000, 'city': 'Phú Quốc'}
2026-04-07 18:01:20,856 | INFO | travelbuddy | Invoking LLM with 8 message(s)
2026-04-07 18:01:24,739 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:01:24,741 | INFO | travelbuddy | Direct response returned
TravelBuddy:
Chào bạn, với ngân sách 5 triệu cho chuyến đi Phú Quốc 2 đêm từ Hà Nội, mình có gợi ý thế này nhé:

Chuyến bay:
*   Bạn có thể chọn chuyến của VietJet Air lúc 16:00 - 18:15 với giá 1.100.000đ (hạng economy).

Ngân sách:
*   Tổng chi cho vé máy bay là 1.100.000đ.
*   Ngân sách còn lại của bạn là 3.900.000đ cho 2 đêm ở Phú Quốc. Như vậy, bạn có thể chi khoảng 1.950.000đ/đêm cho khách sạn.       

Khách sạn:
Dưới đây là một vài lựa chọn khách sạn ở Phú Quốc phù hợp với ngân sách còn lại của bạn, ưu tiên những nơi có đánh giá tốt:
*   **Sol by Meliá** | 4 sao | 1.500.000đ/đêm | Bãi Trường | rating 4.2 (Đây là lựa chọn khá ổn với chất lượng 4 sao và giá cả hợp lý trong ngân sách của bạn)
*   **Lahana Resort** | 3 sao | 800.000đ/đêm | Dương Đông | rating 4.0
*   **9Station Hostel** | 2 sao | 200.000đ/đêm | Dương Đông | rating 4.5 (Nếu bạn muốn tiết kiệm tối đa và thích không gian hostel)  

Bạn thấy sao về những gợi ý này? Có muốn mình tìm thêm thông tin gì không?

================================================================================
TEST CASE 5
USER: 'Tôi muốn đặt khách sạn'
2026-04-07 18:01:24,743 | INFO | travelbuddy | Invoking LLM with 2 message(s)
2026-04-07 18:01:25,928 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:01:25,929 | INFO | travelbuddy | Direct response returned
TravelBuddy:
Tuyệt vời! Bạn muốn đặt khách sạn ở thành phố nào và ngân sách của bạn cho mỗi đêm là bao nhiêu?

================================================================================
TEST CASE 6
USER: 'Giải giúp tôi bài tập linked list'
2026-04-07 18:01:25,931 | INFO | travelbuddy | Invoking LLM with 2 message(s)
2026-04-07 18:01:27,754 | INFO | httpx | HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-04-07 18:01:27,757 | INFO | travelbuddy | Direct response returned
TravelBuddy:
Mình là trợ lý du lịch, chỉ có thể giúp bạn về các vấn đề liên quan đến du lịch như tìm chuyến bay, khách sạn, lên kế hoạch hay tính toán ngân sách thôi. Mình không thể giúp bạn giải bài tập linked list được rồi.

================================================================================
Done.