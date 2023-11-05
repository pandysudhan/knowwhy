import random
import openai


topics = {"human" : [ "brain","human heart"],
          "brain": ["nervous system"],
          "linear algebra": ["ml models"]
          }



def get_topics_list(initial_topic):
    related_topic = initial_topic
    
    topic = initial_topic[0]
    print(topic)
    passion = related_topic.pop()
    while topic.lower() in topics and len(related_topic) <= 5:
        topic = topics[topic]
        topic = random.choice(topic)

        related_topic.append(topic)
    related_topic.append(passion)
    return get_list_and_prod(related_topic)


def get_list_and_prod(topic_list):
    # append openai response to topics list
    res = topic_list
    api_key = "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"
    openai.api_key = api_key




    final_topic = topic_list[-2]
    passion = topic_list[0]


     # Initialize a conversation with a system message
    conversation = [
    {"role": "system", "content": "you  Give response in 5 words max"},
    {"role": "user", "content":"What are some technological advancement(name of specific product: only one) at the" + final_topic + " and " + passion }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    assistant_reply = response['choices'][0]['message']['content']

    res.append(assistant_reply)

    return res