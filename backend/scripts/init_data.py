import sys
sys.path.insert(0, "..")

from app.database import SessionLocal, engine, Base
from app.models.flower import Flower

Base.metadata.create_all(bind=engine)

sample_flowers = [
    {
        "name": "红玫瑰",
        "price": 99.00,
        "image": "https://picsum.photos/seed/rose_red/400/400",
        "description": "经典红玫瑰，象征热烈的爱情，适合表白和纪念日",
        "category": "玫瑰"
    },
    {
        "name": "白玫瑰",
        "price": 89.00,
        "image": "https://picsum.photos/seed/rose_white/400/400",
        "description": "纯洁白玫瑰，象征纯真与美好，适合婚礼和道歉",
        "category": "玫瑰"
    },
    {
        "name": "粉玫瑰",
        "price": 79.00,
        "image": "https://picsum.photos/seed/rose_pink/400/400",
        "description": "温柔粉玫瑰，象征初恋和甜蜜",
        "category": "玫瑰"
    },
    {
        "name": "康乃馨",
        "price": 59.00,
        "image": "https://picsum.photos/seed/carnation/400/400",
        "description": "母亲之花，象征温馨祝福，适合母亲节和长辈生日",
        "category": "康乃馨"
    },
    {
        "name": "向日葵",
        "price": 79.00,
        "image": "https://picsum.photos/seed/sunflower/400/400",
        "description": "阳光积极，活力四射，象征忠诚和热情",
        "category": "向日葵"
    },
    {
        "name": "百合",
        "price": 119.00,
        "image": "https://picsum.photos/seed/lily/400/400",
        "description": "百年好合，美好祝福，适合婚礼和家居装饰",
        "category": "百合"
    },
    {
        "name": "郁金香",
        "price": 109.00,
        "image": "https://picsum.photos/seed/tulip/400/400",
        "description": "高贵典雅，象征爱的宣言和永恒的祝福",
        "category": "郁金香"
    },
    {
        "name": "雏菊",
        "price": 49.00,
        "image": "https://picsum.photos/seed/daisy/400/400",
        "description": "清新可爱，象征纯洁和希望，适合送朋友",
        "category": "雏菊"
    },
]

db = SessionLocal()
try:
    for flower_data in sample_flowers:
        existing = db.query(Flower).filter(Flower.name == flower_data["name"]).first()
        if not existing:
            flower = Flower(**flower_data)
            db.add(flower)
    db.commit()
    print("Initial data inserted successfully.")
except Exception as e:
    print(f"Error: {e}")
    db.rollback()
finally:
    db.close()
