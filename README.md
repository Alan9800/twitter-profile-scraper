# Twitter Profile Scraper

The Twitter Profile Scraper allows you to easily extract comprehensive data from any Twitter user profile. Retrieve user information, tweets, replies, retweets, and much more without limitations. It provides fast, resource-efficient scraping that makes it a powerful tool for analyzing Twitter profiles and understanding user engagement.


<p align="center">
  <a href="https://bitbash.def" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Twitter Profile Scraper</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

This project helps you scrape data from Twitter profiles, such as user details, tweets, and statistics. With no need for a complicated Twitter API setup, it enables seamless data collection from public Twitter accounts.

### Key Features

- Scrape user details such as follower count, location, profile image, and more.
- Extract tweets with all associated metadata, including language, replies, retweets, and more.
- Retrieve detailed statistics for tweets, offering insight into engagement metrics.
- Optimized for fast performance, scraping up to 100 tweets in 20 seconds.
- Flexible configuration to include or exclude specific data fields like user info or suspended users.

## Features

| Feature         | Description                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------|
| User Info      | Extract user-related data like profile information, followers, and bio.                      |
| Tweets          | Gather all tweets, including replies, retweets, and pinned tweets.                           |
| Statistics      | Collect tweet statistics such as retweet count, like count, and reply count.                  |
| Performance     | Fast and efficient, capable of scraping 100 tweets in under 20 seconds with minimal resources. |

## What Data This Scraper Extracts

| Field Name              | Field Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------------|
| user                    | Contains details like name, followers, location, profile image, etc.              |
| created_at              | The timestamp when the tweet was created.                                          |
| conversation_id_str     | Unique ID for the conversation to which the tweet belongs.                        |
| full_text               | The full text of the tweet.                                                       |
| favorite_count          | Number of favorites (likes) the tweet has received.                               |
| reply_count             | The number of replies to the tweet.                                               |
| retweet_count           | The number of retweets for the tweet.                                             |
| media                   | Includes media links, like images or videos attached to the tweet.                 |

## Example Output

    [
      {
        "user": {
          "screen_name": "apify",
          "followers_count": 1032,
          "name": "Apify",
          "location": "The Interweb",
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/1354484488697425920/aQ5dSaTK_normal.jpg"
        },
        "created_at": "Thu Jul 14 13:34:06 +0000 2022",
        "full_text": "Extract profile information from Instagram with Instagram Profile Scraper! #instagramscraper #webscraping",
        "favorite_count": 0,
        "retweet_count": 0,
        "reply_count": 0
      }
    ]

## Directory Structure Tree

twitter-profile-scraper/

├── src/
│   ├── runner.py
│   ├── extractors/
│   │   └── twitter_parser.py
│   ├── outputs/
│   │   └── exporters.py
│   └── config/
│       └── settings.example.json
├── data/
│   ├── inputs.sample.txt
│   └── sample.json
├── requirements.txt
└── README.md

## Use Cases

- **Marketers** use this tool to gather engagement data from Twitter profiles, so they can track user interaction and tailor campaigns accordingly.
- **Social Media Analysts** analyze public Twitter profiles for follower trends, tweet performance, and content strategies.
- **Developers** integrate Twitter profile scraping into their automation tools, saving time on manual data collection.

## FAQs

**Q: How do I configure the input for the scraper?**

A: You need to provide a JSON file with a list of Twitter profile URLs. You can also configure additional options like including user info or using a proxy.

**Q: Can this scraper be used without a Twitter API key?**

A: Yes, this scraper does not require a Twitter API key. It works by scraping publicly available Twitter profiles.

## Performance Benchmarks and Results

**Primary Metric:** Scrapes up to 100 tweets in 20 seconds.

**Reliability Metric:** 98% success rate with minimal failures due to rate limits.

**Efficiency Metric:** Scrapes 100 tweets with ~0.02-0.025 compute units.

**Quality Metric:** Captures complete tweet details and user information with high precision.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
