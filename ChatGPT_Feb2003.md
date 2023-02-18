ChatGPT (February 2023)

There is a lot of hype around the WeakAI ChatGPT (and the whole GPT family) which is producing a human-like text from a provided question (A variant of GPT-3 is used for GitHub Copilot). GPT means 'Generative Pre-trained Transformer'. The 'pre-training' is a key technique enabling production of human like answers. This pre-training comes at a tremendous cost and it is unsupervised by humans, loosely speaking it consists in the following: given a list of words ('token') try to guess the next one, and after you can generalize that to sentences/paragraphs creating context/concepts and then enabling a good understanding of a language. Most of the input data for the pre-training comes from the 'Common Crawl' organization, which is crawling the whole Internet and generates around 100 TB to 300 TB of data monthly, the WebText2 dataset, few Books datasets and the whole Wikipedia. It costs a few millions to a few tens of millions in training cost only, about a few months in the best case to prepare the data, a staff of few tenth of engineers. The data center needs to handle few thousands to few ten of thousands of top notch GPUs, you need to take in account the few petabytes in storage to feed the system and the time to gather it from the Internet...etc... With a big spoon, you can say a full iteration will take around few months to 12 months in such systems, an increment probably around a few weeks on the pretraining only.
There are interesting issues related to this system. First, there is a large set of 'safeguard' rules that have been implemented to prevent 'bad' or 'dangerous' uses of the system, which can be already be bypassed by various means. Another fundamental part is the 'reward' used during the training of the system, which is kind of 'does the human like my answer ?'. I am taking a short-cut but you can think of the system as a kind of 'yes man': in other words instead of telling you it is wrong, it may produce something wrong to make you like the answer. Following that, if something provided is wrong or misleading, it may provide a 'kind' lie to make you like the answer. ChatGPT has no sense of what is good/bad, the truth/the lie, so by having this kind of 'pleasing' answer delivered to the human as a metric, it can be potentially 'dangerous'. Also, introducing those rules introduced a strong bias too, the system is enforced to answer 'nicely', even if it knows the answer, if it displease you, it may be a 'silent lie' provided with a nice kind answer. So, you have to challenge and to verify the answers of such systems.

Still, it is an important milestone in our era making the public aware of the capabilities of such systems, but you have to be more attentive and more cautious about what such system is producing.


Basic example during a session with ChatGPT where something wrong was provided in its answer.

Julien Boucaron
How a greenhouse keeps heat ?

A greenhouse is designed to trap and retain heat from the sun, creating a warm and protected environment for plants to grow. It works on the principle of the greenhouse effect, where sunlight enters the greenhouse and is converted to heat energy, which is then trapped inside the structure.

The walls and roof of a greenhouse are made of transparent materials, such as glass or plastic, which allow sunlight to pass through. The sunlight heats up the plants, soil, and other objects inside the greenhouse, which then radiate heat in the form of infrared radiation.

However, the transparent walls and roof also allow some of the heat to escape. To prevent heat loss, a greenhouse is designed to be well-insulated, with double-glazed windows or inflated plastic sheets that create a layer of air between the inside and outside of the greenhouse.

Additionally, the soil in the greenhouse is often covered with a layer of mulch or other insulating material to help retain heat. Some greenhouse designs also include thermal mass, such as water tanks or concrete floors, which absorb and store heat during the day and release it at night to maintain a consistent temperature.

Overall, a greenhouse is designed to create a warm and stable environment for plants to grow by trapping and retaining heat from the sun.




Julien Boucaron
Actually this is wrong a greenhouse is blocking the convection and it is not based on the greenhouse effect.


You are correct that the mechanism by which a greenhouse keeps heat is not primarily based on the greenhouse effect, but rather on the physical principle of blocking convection.

A greenhouse works by trapping warm air inside the structure and preventing it from escaping through convection. The walls and roof of a greenhouse are made of materials that are transparent to sunlight but opaque to infrared radiation, which is the type of radiation that is emitted by warm objects.

When sunlight enters the greenhouse, it heats up the air and the objects inside. As the warm air rises, it comes into contact with the cooler surface of the walls and roof, and begins to lose heat through conduction. However, the transparent walls and roof also prevent the warm air from escaping through convection, which is the transfer of heat through the movement of fluid, such as air or water.

By blocking convection, a greenhouse is able to maintain a warm and stable environment for plants to grow, even when the outside temperature is much colder. The insulating properties of the greenhouse can be enhanced by using double-glazed windows, insulating curtains, or other materials that reduce heat loss.

While the greenhouse effect does play a role in warming the inside of a greenhouse, it is not the primary mechanism by which a greenhouse retains heat.




Julien Boucaron
Why did you not talk about convection in the initial answer ?

I apologize for the error in my initial answer. Thank you for bringing it to my attention.

As an AI language model, I strive to provide accurate and helpful answers to the best of my knowledge and capabilities. However, I may occasionally make mistakes or oversights.

In the case of my initial answer regarding how a greenhouse keeps heat, I provided an explanation based on the greenhouse effect, which is not the primary mechanism by which a greenhouse retains heat. I should have mentioned the role of convection in more detail, as it is an essential part of the process.

Again, I apologize for any confusion my initial answer may have caused and I appreciate your effort in bringing it to my attention. If you have any further questions or concerns, please feel free to ask.





