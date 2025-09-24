import os
from typing import Optional

import serpapi
from pydantic import BaseModel, Field
from langchain_core.tools import tool

# from pydantic import BaseModel, Field


class HotelsInput(BaseModel):
    q: str = Field(description='Location of the hotel')
    check_in_date: str = Field(description='Check-in date. The format is YYYY-MM-DD. e.g. 2024-06-22')
    check_out_date: str = Field(description='Check-out date. The format is YYYY-MM-DD. e.g. 2024-06-28')
    sort_by: Optional[str] = Field(8, description='Parameter is used for sorting the results. Default is sort by highest rating')
    adults: Optional[int] = Field(1, description='Number of adults. Default to 1.')
    children: Optional[int] = Field(0, description='Number of children. Default to 0.')
    rooms: Optional[int] = Field(1, description='Number of rooms. Default to 1.')
    hotel_class: Optional[str] = Field(
        None, description='Parameter defines to include only certain hotel class in the results. for example- 2,3,4')


class HotelsInputSchema(BaseModel):
    params: HotelsInput


@tool(args_schema=HotelsInputSchema)
def hotels_finder(params: HotelsInput):
    '''
    Find hotels using the Google Hotels engine.

    Returns:
        dict: Hotel search results.
    '''

    # 检查是否配置了SerpAPI
    api_key = os.environ.get('SERPAPI_API_KEY')
    if not api_key or api_key == 'your_serpapi_api_key_here':
        # 返回模拟酒店数据
        return [
            {
                "name": "上海和平饭店",
                "description": "历史悠久的豪华酒店，位于外滩核心地段，享有黄浦江美景",
                "rate_per_night": {"lowest": "$180", "extracted_lowest": 180},
                "total_rate": {"lowest": "$720", "extracted_lowest": 720},
                "nearby_places": [{"name": "外滩", "transportations": [{"type": "Walking", "duration": "2 min"}]}],
                "hotel_class": "5星级",
                "reviews": 4.5,
                "reviews_count": 2891,
                "images": [{"thumbnail": "https://example.com/hotel1.jpg"}],
                "link": "https://www.google.com/travel/hotels",
                "amenities": ["免费WiFi", "健身房", "游泳池", "商务中心", "餐厅"]
            },
            {
                "name": "上海浦东丽思卡尔顿酒店",
                "description": "位于陆家嘴金融区的奢华酒店，俯瞰黄浦江和城市天际线",
                "rate_per_night": {"lowest": "$220", "extracted_lowest": 220},
                "total_rate": {"lowest": "$880", "extracted_lowest": 880},
                "nearby_places": [{"name": "东方明珠", "transportations": [{"type": "Walking", "duration": "5 min"}]}],
                "hotel_class": "5星级",
                "reviews": 4.7,
                "reviews_count": 1654,
                "images": [{"thumbnail": "https://example.com/hotel2.jpg"}],
                "link": "https://www.google.com/travel/hotels",
                "amenities": ["免费WiFi", "Spa", "健身房", "商务中心", "礼宾服务"]
            },
            {
                "name": "上海静安香格里拉大酒店",
                "description": "位于静安区的现代化豪华酒店，交通便利，购物方便",
                "rate_per_night": {"lowest": "$160", "extracted_lowest": 160},
                "total_rate": {"lowest": "$640", "extracted_lowest": 640},
                "nearby_places": [{"name": "静安寺", "transportations": [{"type": "Walking", "duration": "3 min"}]}],
                "hotel_class": "4星级",
                "reviews": 4.4,
                "reviews_count": 2156,
                "images": [{"thumbnail": "https://example.com/hotel3.jpg"}],
                "link": "https://www.google.com/travel/hotels",
                "amenities": ["免费WiFi", "游泳池", "健身房", "餐厅", "会议室"]
            }
        ]

    # 构建SerpAPI搜索参数
    search_params = {
        'api_key': api_key,
        'engine': 'google_hotels',
        'hl': 'en',
        'gl': 'us',
        'q': params.q,
        'check_in_date': params.check_in_date,
        'check_out_date': params.check_out_date,
        'currency': 'USD',
        'adults': params.adults,
        'children': params.children,
        'rooms': params.rooms,
        'sort_by': params.sort_by,
        'hotel_class': params.hotel_class
    }

    
    try:
        search = serpapi.search(search_params)
        results = search.data
        properties = results.get('properties', [])
        if not properties:
            return "未找到符合条件的酒店，请尝试调整搜索条件。"
        return properties[:5]
    except Exception as e:
        print(f"SerpAPI酒店搜索失败: {str(e)}")
        return f"酒店搜索失败: {str(e)}。请检查网络连接和API配置。"
