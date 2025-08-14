import random


music_suggestions = {
    "happy": {
        "genre": "Pop",
        "examples": [
            "Viva La Vida – Coldplay",
            "Treasure – Bruno Mars",
            "Levitating – Dua Lipa",
            "Style – Taylor Swift",
            "There's Nothing Holdin' Me Back – Shawn Mendes",
        ],
    },
    "sad": {
        "genre": "Soft Rock / Ballads",
        "examples": [
            "The Scientist – Coldplay",
            "Young and Beautiful – Lana Del Rey",
            "Happier – Ed Sheeran",
            "Back To December – Taylor Swift",
            "Sign of the Times – Harry Styles",
        ],
    },
    "stressed": {
        "genre": "Lo-fi / Chill",
        "examples": [
            "Sunflower – Rex Orange County",
            "Delicate – Taylor Swift",
            "Love Me Like You Do (Acoustic) – Ellie Goulding",
            "Video Games – Lana Del Rey",
            "Gravity – John Mayer",
        ],
    },
    "bored": {
        "genre": "Dance / Electronic",
        "examples": [
            "Something Just Like This – The Chainsmokers & Coldplay",
            "Electricity – Dua Lipa & Silk City",
            "Finesse – Bruno Mars",
            "End Game – Taylor Swift",
            "Higher Love – Kygo & Whitney Houston",
        ],
    },
    "romantic": {
        "genre": "Love Ballads / Soft Pop",
        "examples": [
            "All of Me – John Legend",
            "Perfect – Ed Sheeran",
            "Call It What You Want – Taylor Swift",
            "Lovely – Billie Eilish & Khalid",
            "Adore You – Harry Styles",
        ],
    },
    "energetic": {
        "genre": "Rock / EDM",
        "examples": [
            "Radioactive – Imagine Dragons",
            "Can't Stop the Feeling! – Justin Timberlake",
            "...Ready For It? – Taylor Swift",
            "24K Magic – Bruno Mars",
            "I Feel It Coming – The Weeknd",
        ],
    },
    "workout": {
        "genre": "High-Energy Pop / EDM",
        "examples": [
            "Believer – Imagine Dragons",
            "Blinding Lights – The Weeknd",
            "Treasure – Bruno Mars",
            "Shake It Off – Taylor Swift",
            "Closer – The Chainsmokers",
        ],
    },
    "weekend": {
        "genre": "Party Pop / Chill Vibes",
        "examples": [
            "Save Your Tears – The Weeknd",
            "Don't Start Now – Dua Lipa",
            "Treasure – Bruno Mars",
            "Delicate – Taylor Swift",
            "Blue Jeans – Lana Del Rey",
        ],
    },
    "chill": {
        "genre": "Lo-fi / Soft Pop",
        "examples": [
            "Cardigan – Taylor Swift",
            "Summertime Sadness – Lana Del Rey",
            "Let Somebody Go – Coldplay & Selena Gomez",
            "Love In The Dark – Adele",
            "Falling – Harry Styles",
        ],
    },
}

combined_weekend_chill = list(
    set(
        music_suggestions["weekend"]["examples"]
        + music_suggestions["chill"]["examples"]
    )
)
music_suggestions["weekend"]["examples"] = combined_weekend_chill
music_suggestions["chill"]["examples"] = combined_weekend_chill


def recommend_music(mood):
    mood = mood.lower()
    if mood in music_suggestions:
        genre = music_suggestions[mood]["genre"]
        songs = music_suggestions[mood]["examples"]
        suggestion = random.choice(songs)

        print(f"\n🎭 Mood detected: {mood.capitalize()}")
        print(f"🎵 Recommended Genre: {genre}")
        print(f"▶ Try listening to: {suggestion}")
    else:
        print("Sorry, I don't have suggestions for that mood yet.")


print("🎶 Welcome to Mood-to-Music Recommender 🎶")
user_mood = input("How are you feeling today? ").strip()
recommend_music(user_mood)
