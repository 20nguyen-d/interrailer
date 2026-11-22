import random

subjectLibrary = {
    "Maths": [
        "Sequences and Series",
        "Functions 1",
        "Polynomials, Equations and Inequalities",
        "Trigonometry 1",
        "Probability",
        "Differentiation 1",
        "Single Variable Statistics",
        "Permutations and Combinations",
        "Discrete Random Variables",
        "Trigonometry 2",
        "Exponential Functions",
        "Differentiation 2"
    ],

    "Computer Science": [
        "A1.1 Computer hardware and Operation",
        "A1.2 Data representation and computer logic",
        "A1.3 Operating systems and control Systems",
        "A1.4 Translation",
        "A3.1 Database Fundamentals",
        "A3.2 Database Design",
        "A3.3 Database Programming",
        "A3.4 Alternative databases and data warehouses",
        "A4.1 Machine learning fundamentals",
        "A4.2 Data preprocessing",
        "A4.3 Machine learning approaches",
        "A4.4 Ethical considerations"
    ]
}


topicScores = {}

for x in subjectLibrary:
    topicScores[x] = {}
    for topic in subjectLibrary[x]:
        topicScores[x][topic] = 0


def chooseTopic():

    allTopics = []
    weights = []
    for subject, topics in topicScores.items():
        for topic, score in topics.items():
            allTopics.append([subject, topic])

            weight = 1/(score+1)
            weights.append(weight)

    return random.choices(allTopics, weights=weights, k=1)[0]

def reviseTopic():
    subject, topic = chooseTopic()
    print("go revise {}, topic: {}".format(subject, topic))
    print("current topic score is: {}".format(topicScores[subject][topic]))

    done = input("so did you revise it?? (y/n)").lower()
    if done == "y":
        topicScores[subject][topic] += 1
        print("updated score for subject {} topic {} is {}".format(subject, topic, topicScores[subject][topic]))
    else:
        print("score unchanged for subject {} topic {} which is {}".format(subject, topic, topicScores[subject][topic]))


while True:
    reviseTopic()
    again = input("another topic ?? (y/n)").lower()
    if again != "y":
        break

print("well done!! Your final scores are: ")

for subject, topics in topicScores.items():
    print("\n{}:".format(subject))
    for topic, score in topics.items():
        print(" {}:  {}".format(topic, score))