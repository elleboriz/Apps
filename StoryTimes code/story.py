from flask import Flask , render_template ,url_for
#from storylines import lines
app = Flask(__name__)

@app.route("/")
@app.route("/homepage")
def StoryTimes_home():
    return render_template("home.html")

@app.route("/stories")
def StoryTimes_story():
    stories = [{
        "id":1,
        "category": "Morals",
        "img": r"https://github.com/elleboriz/Apps/blob/main/StoryTimes%20code/assets/the-boy-who-cried-wolf-min.jpeg?raw=true",
        "title": "The boy who Cried wolf",
        "body": "Once, there was a boy who became bored when he watched over the village sheep grazing on the hillside. To entertain himself, he sang out, wolf! Wolf! The wolf is chasing the sheep!  When the villagers heard the cry, they came running up the hill to drive the wolf away. But, when they arrived, they saw no wolf. The boy was amused when seeing their angry faces.  Dont scream wolf, boy, warned the villagers, when there is no wolf! They angrily went back down the hill.  Later, the shepherd boy cried out once again, wolf! Wolf! The wolf is chasing the sheep! To his amusement, he looked on as the villagers came running up the hill to scare the wolf away. As they saw there was no wolf, they said strictly, save your frightened cry for when there really is a wolf! Dont cry wolf when there is no wolf! But the boy grinned at their words while they walked grumbling down the hill once more.  Later, the boy saw a real wolf sneaking around his flock. Alarmed, he jumped on his feet and cried out as loud as he could, wolf! Wolf! But the villagers thought he was fooling them again, and so they didnt come to help.  At sunset, the villagers went looking for the boy who hadnt returned with their sheep. When they went up the hill, they found him weeping.  There really was a wolf here! The flock is gone! I cried out, wolf! But you didnt come, he wailed.  An old man went to comfort the boy. As he put his arm around him, he said, nobody believes a liar, even when he is telling the truth!"
    }, {
        "id": 2,
        "category": "Morals",
        "img": r"https://github.com/elleboriz/Apps/blob/main/StoryTimes%20code/assets/King%20midas%20and%20The%20Golden%20Touch-min.png?raw=true",
        "title": "The Golden Touch",
        "body": "There once was a king named midas who did a good deed for a satyr (the demi God). And he was then granted a wish by dionysus God of Prosperity , fertility ,and winemaking.  For his wish, midas asked that whatever he touched would turn to gold. Despite dionysus' efforts to prevent it, midas pleaded that this was a fantastic wish, and so, it was bestowed.  Excited about his newly-earned powers, midas started touching all kinds of things, turning each item into pure gold.  But soon, midas became hungry. As he picked up a piece of food, he found he couldn't eat it. It had turned to gold in his hand.  Hungry, midas groaned, `i'll starve! Perhaps this was not such an excellent wish after all! `  seeing his dismay, midas' beloved daughter threw her arms around him to comfort him, and she, too, turned to gold. `the golden touch is no blessing, ` midas cried ."}
    ]
    return render_template("stories.html",stories = stories)


