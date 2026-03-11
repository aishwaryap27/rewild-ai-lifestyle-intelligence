
import pandas as pd
import random
random.seed(42)
categories = [
    "dopamine_detox",
    "minimalism",
    "fitness",
    "slow_living",
    "burnout_recovery"
]
captions = [
    "deleted all my apps, feeling free",

    "minimalist morning routine no phone",
    "30 day dopamine detox challenge day 1",
    "slow morning coffee no screens",
    "gym over doom scrolling every time",
    "bought nothing this week, proud of it",
    "analog journaling changed my life",
    "screen free sunday is my religion",
    "less notifications more presence",
    "running at 6am beats social media",
]

data={
"post_id": range(1,201),"caption":[random.choice(captions) for _ in range(200)],
"category":[random.choice(categories) for_ in range(200)],
"likes": [random.randint(10,5000) for _ in range(200)],
"comments": [random.randint(1,300) for _ in range(200)],
"shares": [random.randint(0,150) for _ in range(200)],
"engagement_score":[random.uniform(0.1,9.9) for_ in range(200)],
"days":list(range(1,201))

}
df=pd.DataFrame(data)
df.to_csv("data/sample_posts.csv",index=False)
print("dataset created succesfully")

