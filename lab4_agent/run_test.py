import traceback
from agent import graph

TEST_CASES = [
    "Hello",
    "Xin chào, tôi muốn đi du lịch nhưng chưa biết đi đâu",
    "Tìm giúp tôi chuyến bay từ Hà Nội đến Đà Nẵng",
    "Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp tôi!",
    "Tôi muốn đặt khách sạn",
    "Giải giúp tôi bài tập linked list",  # case phải bị từ chối
]

def print_divider():
    print("\n" + "=" * 80)
def extract_text(message):
    content = getattr(message, "content", message)

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                parts.append(item.get("text", ""))
            else:
                parts.append(str(item))
        return "\n".join(part for part in parts if part)

    return str(content)
for i, user_input in enumerate(TEST_CASES, 1):
    print_divider()
    print(f"TEST CASE {i}")
    print(f"USER: {repr(user_input)}")

    if not user_input.strip():
        print("SKIP: input rỗng")
        continue

    try:
        result = graph.invoke({"messages": [("human", user_input)]})
        last_message = result["messages"][-1]
        print("TravelBuddy:")
        print(extract_text(last_message))
    except Exception as e:
        print("ERROR:")
        print(e)
        traceback.print_exc()

print_divider()
print("Done.")