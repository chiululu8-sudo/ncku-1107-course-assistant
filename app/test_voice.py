import asyncio
import os
import sys

sys.path.append(r"E:\Gemin bak\ncku_course_assistant\app")
import server

async def test():
    url = await server.generate_speech_file("同學你好，我是成大課堂的雲哲助教。我們現在用的是微軟高品質真人神經語音，聽起來完全不生硬，非常自然！", "yunjhe")
    print("生成成功！URL:", url)
    print("實體檔案存在:", os.path.exists(os.path.join(r"E:\Gemin bak\ncku_course_assistant", url.lstrip("/"))))

if __name__ == "__main__":
    asyncio.run(test())
