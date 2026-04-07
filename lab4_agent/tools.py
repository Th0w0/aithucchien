from langchain_core.tools import tool


FLIGHTS_DB = {
    ("Hà Nội", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "07:20", "price": 1_450_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "14:00", "arrival": "15:20", "price": 2_800_000, "class": "business"},
        {"airline": "VietJet Air", "departure": "08:30", "arrival": "09:50", "price": 890_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "11:00", "arrival": "12:20", "price": 1_200_000, "class": "economy"},
    ],

    ("Hà Nội", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "07:00", "arrival": "09:15", "price": 2_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "10:00", "arrival": "12:15", "price": 1_350_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "16:00", "arrival": "18:15", "price": 1_100_000, "class": "economy"},
    ],

    ("Hà Nội", "Hồ Chí Minh"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "08:10", "price": 1_600_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "07:30", "arrival": "09:40", "price": 950_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "12:00", "arrival": "14:10", "price": 1_300_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "18:00", "arrival": "20:10", "price": 3_200_000, "class": "business"},
    ],

    ("Hồ Chí Minh", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "09:00", "arrival": "10:20", "price": 1_300_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "13:00", "arrival": "14:20", "price": 780_000, "class": "economy"},
    ],

    ("Hồ Chí Minh", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "08:00", "arrival": "09:00", "price": 1_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "15:00", "arrival": "16:00", "price": 650_000, "class": "economy"},
    ],
}

# ================================================================

HOTELS_DB = {
    "Đà Nẵng": [
        {"name": "Mường Thanh Luxury", "stars": 5, "price_per_night": 1_800_000, "area": "Mỹ Khê", "rating": 4.5},
        {"name": "Sala Danang Beach", "stars": 4, "price_per_night": 1_200_000, "area": "Mỹ Khê", "rating": 4.3},
        {"name": "Fivitel Danang", "stars": 3, "price_per_night": 650_000, "area": "Sơn Trà", "rating": 4.1},
        {"name": "Memory Hostel", "stars": 2, "price_per_night": 250_000, "area": "Hải Châu", "rating": 4.6},
        {"name": "Christina's Homestay", "stars": 2, "price_per_night": 350_000, "area": "An Thượng", "rating": 4.7},
    ],

    "Phú Quốc": [
        {"name": "Vinpearl Resort", "stars": 5, "price_per_night": 3_500_000, "area": "Bãi Dài", "rating": 4.4},
        {"name": "Sol by Meliá", "stars": 4, "price_per_night": 1_500_000, "area": "Bãi Trường", "rating": 4.2},
        {"name": "Lahana Resort", "stars": 3, "price_per_night": 800_000, "area": "Dương Đông", "rating": 4.0},
        {"name": "9Station Hostel", "stars": 2, "price_per_night": 200_000, "area": "Dương Đông", "rating": 4.5},
    ],

    "Hồ Chí Minh": [
        {"name": "Rex Hotel", "stars": 5, "price_per_night": 2_800_000, "area": "Quận 1", "rating": 4.3},
        {"name": "Liberty Central", "stars": 4, "price_per_night": 1_400_000, "area": "Quận 1", "rating": 4.1},
        {"name": "Cochin Zen Hotel", "stars": 3, "price_per_night": 550_000, "area": "Quận 3", "rating": 4.4},
        {"name": "The Common Room", "stars": 2, "price_per_night": 180_000, "area": "Quận 1", "rating": 4.6},
    ],
}


@tool
def search_flights(origin: str, destination: str) -> str:
    """
    Dùng khi người dùng muốn tìm chuyến bay giữa hai thành phố.

    Input:
    - origin: Thành phố xuất phát (ví dụ: "Hà Nội")
    - destination: Thành phố điểm đến (ví dụ: "Đà Nẵng")

    Output:
    - Danh sách các chuyến bay dưới dạng text, mỗi dòng gồm:
      hãng bay | giờ đi - giờ đến | giá | hạng ghế

    Lưu ý:
    - Dùng tool này khi user hỏi về chuyến bay, vé máy bay, di chuyển bằng máy bay.
    - Kết quả có thể dùng để chọn chuyến bay và lấy giá phục vụ tính ngân sách.
    """
    key = (origin, destination)

    if key in FLIGHTS_DB:
        flights = FLIGHTS_DB[key]
    elif (destination, origin) in FLIGHTS_DB:
        flights = FLIGHTS_DB[(destination, origin)]
    else:
        return f"Không tìm thấy chuyến bay từ {origin} đến {destination}."
    flights.sort(key=lambda x: x["price"])
    flights = flights[:3]

    result = []
    for f in flights:
        price = f"{f['price']:,}".replace(",", ".") + "đ"
        result.append(
            f"{f['airline']} | {f['departure']} - {f['arrival']} | {price} | {f['class']}"
        )

    return "\n".join(result)

@tool
def search_hotels(city: str, max_price_per_night: int = 99999999, sort_by: str = "rating") -> str:
    """
    Dùng khi người dùng muốn tìm khách sạn tại một thành phố.

    Input:
    - city: Thành phố cần tìm khách sạn (ví dụ: "Đà Nẵng")
    - max_price_per_night: Giá tối đa mỗi đêm (dùng để lọc theo ngân sách)
    - sort_by:
        + "rating" (mặc định): sắp xếp theo đánh giá cao → thấp
        + "price": sắp xếp theo giá rẻ → đắt

    Output:
    - Danh sách khách sạn dưới dạng text, mỗi dòng gồm:
      tên | số sao | giá/đêm | khu vực | rating

    Lưu ý:
    - Dùng sau khi đã xác định ngân sách hoặc sau khi chọn chuyến bay.
    - max_price_per_night nên dựa trên ngân sách còn lại.
    """
    if city not in HOTELS_DB:
        return f"Không có dữ liệu khách sạn tại {city}."

    hotels = [
        h for h in HOTELS_DB[city]
        if h["price_per_night"] <= max_price_per_night
    ]

    if not hotels:
        return f"Không tìm thấy khách sạn tại {city} với giá dưới {max_price_per_night:,}đ."

    # 🔥 Sorting logic
    if sort_by == "price":
        hotels.sort(key=lambda x: x["price_per_night"])
    else:  # default = rating
        hotels.sort(key=lambda x: x["rating"], reverse=True)

    result = []
    for h in hotels:
        price = f"{h['price_per_night']:,}".replace(",", ".") + "đ"
        result.append(
            f"{h['name']} | {h['stars']}⭐ | {price}/đêm | {h['area']} | rating {h['rating']}"
        )

    return "\n".join(result)

@tool
def  calculate_budget(total_budget: int, expenses: str) -> str:
    """
    Dùng để tính toán ngân sách chuyến đi.

    Input:
    - total_budget: Tổng ngân sách (ví dụ: 5_000_000)
    - expenses: Chuỗi chi phí dạng:
        "vé_máy_bay:900000,khách_sạn:650000"

    Output:
    - Bảng chi phí gồm:
        + từng khoản chi
        + tổng chi
        + ngân sách
        + số tiền còn lại hoặc vượt ngân sách

    Lưu ý:
    - Dùng sau khi đã chọn chuyến bay hoặc khách sạn.
    - Kết quả giúp quyết định bước tiếp theo (chọn khách sạn phù hợp ngân sách).
    """
    try:
        items = expenses.split(",")
        parsed = {}

        for item in items:
            name, value = item.split(":")
            parsed[name.strip()] = int(value.strip())

        total_spent = sum(parsed.values())
        remaining = total_budget - total_spent

        def fmt(x):
            return f"{x:,}".replace(",", ".") + "đ"

        lines = ["Bảng chi phí:"]
        for k, v in parsed.items():
            lines.append(f"- {k}: {fmt(v)}")

        lines.append("---")
        lines.append(f"Tổng chi: {fmt(total_spent)}")
        lines.append(f"Ngân sách: {fmt(total_budget)}")
        lines.append(f"Còn lại: {fmt(remaining)}")

        if remaining < 0:
            lines.append(f"⚠️ Vượt ngân sách {fmt(abs(remaining))}!")

        return "\n".join(lines)

    except:
        return "Format expenses không hợp lệ. Dùng dạng: vé_máy_bay:900000,khách_sạn:650000"

