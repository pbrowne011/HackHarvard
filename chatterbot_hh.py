import re
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot('Ron Obvious')


blog_post = '''Robert Wiblin: Hi listeners, this is the 80,000 Hours Podcast, where each week we have an unusually in-depth conversation about one of the world’s most pressing problems and how you can use your career to solve it. I’m Rob Wiblin, Director of Research at 80,000 Hours.

If not for Toby Ord I probably wouldn’t be doing what I’m doing today. It’s he who recruited Will MacAskill, and the two of them then went on to get the ball rolling on the effective altruism and longtermism movements as we see them today.

I love Toby Ord’s new book, The Precipice: Existential Risk & The Future of Humanity. It’s now the first thing I’ll be giving people if they want to read a book that explains what I do and what 80,000 Hours recommends.

The book is out March 5th in the UK and March 24th in the USA, and in audiobook form and we’ll link to places you can get it in the show notes or you can find out at theprecipice.com.

Even if you think you know a lot about the ways civilization could go off the rails or how it might flourish more than we ever thought, there’s a tonne of new stuff to learn in this book — scientific details about each scenario, and new methods for sensibly analysing them.

Toby is a famously good explainer of complex issues — a bit of a modern Carl Sagan character — so as expected we got a great interview out of him and barely even had to work for it.

We start by talking about the ways things could go badly but get to how things could go amazingly at the end of the episode.

As for all our long interviews, we have chapters which you can use to skip to the section of conversation you want to hear, if your podcast software supports chapters. For example, this episode is coming out during a moment of serious panic about COVID-19 so perhaps you’d like to skip to the section called ‘biological threats’ that comes halfway through.

Finally, people have loved Arden’s contributions to the show so far and due to popular demand she’s back for this interview too.

Alright, without further ado, here’s Toby Ord.

The interview begins [00:02:15]
Robert Wiblin: Today, I’m speaking with Dr. Toby Ord, a moral philosopher at Oxford University. His work focuses on the big picture questions facing humanity. His early work explored the ethics of global health and global poverty and this led him to create an international society called Giving What We Can whose members have pledged over $1 billion to the most effective charities that they can find. He was also influential in the creation of the wider effective altruism movement and as a result has been a trustee of 80,000 Hours since its foundation. Toby’s advised the World Health Organization, The World Bank, The World Economic Forum, the US National Intelligence Council, the UK Prime Minister’s Office, the Cabinet Office, and the Government Office for Science. But today he’s here to discuss his new book, “The Precipice: Existential Risk and the Future of Humanity”, which makes the case that protecting humanity’s future is the central challenge of our time. Thanks so much for coming on the podcast, Toby.

Toby Ord: It’s great to be here, Rob.

Robert Wiblin: And we’re also joined again by my research colleague here at 80,000 Hours, Arden Koehler who will be finishing her PhD in philosophy at NYU any day now.

Arden Koehler: Rob, don’t say that out loud on air! It’s great to be here. I really enjoyed the book a lot. I liked how it combined a sort of rigorous empirical analysis of different risks that we face with a case for why we should take this stuff seriously.

Toby Ord: Thanks.

Arden Koehler: So usually we ask guests what they’re working on now and why they think it’s really important. But since you have just finished this book, I guess we know what you’ve been working on. So why don’t you tell us a little bit about the project and why you think it’s important?

Toby Ord: Sure. The book is called, “The Precipice: Existential Risk and the Future of Humanity”, and it’s about how humanity has been around for 2000 centuries so far and how long and great our future might be and how soaring our potential is, but how all of this is at risk. There have been natural risks of human extinction: things like asteroids that could potentially wipe us out as they have many other species. And there’s been this background rate of such risks. But with humanity’s increasing power over time, our rise of technological power, we’ve reached this stage where we may have the power to destroy ourselves leading to the destruction, not only of the present, but of the entire future and everything that we could hope to achieve. And this is a time that I call “The Precipice” and the book is therefore looking at extinction risks and other forms of existential risk.

Toby Ord: But it’s doing so because I’m inspired by the hope for the future and what we might be able to achieve if we can make it through this time. So the book covers the history of humanity, the potential future of humanity, the questions about the ethics of why we might care so much about our future and safeguarding it, and then also gets into the science behind the risks. It gets into interesting methodological and technical tools for thinking about these risks and then also policy questions and what individuals might be able to do or what humanity might be able to do about these risks and then what we could achieve if we get through this time.

What Toby learned while writing the book [00:05:04]
Robert Wiblin: So you and I spoke about the book or, I guess, especially the philosophy and ethics part of the book… I guess it was two and a half years ago, back in 2017; I think it was in episode six. You must have spent quite a lot of the last two and a half years researching for the book. Is there anything that you changed your mind about that’s significant?

Toby Ord: Yeah. One of the main areas concerns climate change. I thought this was the kind of thing where one could show fairly clearly that climate change can’t be much of an existential risk, that it could be absolutely terrible and something that’s very important to avoid and potentially with a risk of global catastrophe, but that it wouldn’t really pose much existential risk and over time I think that it’s harder to show that than I’d thought. We can get into that more later.

Robert Wiblin: Yeah, we’ll get back to the climate change section later. Is there anything that you learned that particularly surprised you that came out of left field?

Toby Ord: Yeah, actually one such thing was when looking at asteroid risk and the different ways we have of diverting asteroids from hitting the Earth, I was very surprised to learn that none of the methods actually applied to asteroids at the size scales that would threaten existential catastrophe. All of the conversation about gravity tugs and reflective methods, or nuclear methods and things, were all about asteroids that would cause local catastrophes rather than the global ones.

Robert Wiblin: Oh, so those other ones are just too big for those methods to work?

Toby Ord: Yeah.

Robert Wiblin: We’d need something else?

Toby Ord: We would need something else. That was a little bit alarming because a lot of the general public interest as well as my particular interest about the risk from asteroids or comets, concerns the ones that could cause an extinction threat. And yes, I was quite surprised to learn that the deflection techniques don’t really apply to those.

Arden Koehler: Yeah. Was it just because it was easier to try to address these smaller threats and so they went for that because it was somewhat close by in genre to the larger threats?

Toby Ord: Yeah, I mean I don’t really blame the scientists or engineers for this. I think they were just trying to work out how to deflect asteroids, and it turns out it’s harder to deflect the ones that are bigger. The ones that, for example, are 10 kilometers across are 10 times the size of the ones that are one kilometer across. Well, at least we say 10 times the size. But they’re a thousand times the volume and a thousand times the mass. And so techniques that involve changing the momentum of this thing is a thousand times harder. So it is just extremely difficult to do this. And also, the risk, or at least the probability of being hit by the bigger ones, is really much smaller than of these ones that could cause local catastrophes. So often people who are not particularly focused on existential risk see that one other thing might be 10,000 times as likely and then they think it’s not at all unreasonable to spend a lot of effort trying to focus on that situation. But there’s a lack of communication about the fact that it only applies to one of these size ranges.

Robert Wiblin: Okay. Just to map out where I think the conversation will go: the rough structure; I think first we should talk about a bunch of specific existential risks. So nuclear war, climate change, that kind of thing. Then maybe zoom out and talk about existential risks as a whole. Then maybe we can push back a little bit on the idea that existential risk is particularly high or that we’re living in a particularly important time in human history: see what the counterarguments are. And then maybe close by thinking about what a good future might actually look like and what the social barriers might be to getting there. Is that good?

Toby Ord: Yeah.

Arden Koehler: Sounds good.

Estimates for specific x-risks [00:08:10]
Robert Wiblin: All right. So I wanted to start by going through this menagerie of potential threats that we face because I think this is something that readers might potentially really love about the book even if they know quite a bit about existential risk as a whole and I imagine some listeners are fairly familiar with the general topic by this point. Yeah, really go through this list quite methodically. Just describing the science and the history behind each one of them and trying to figure out how much of a threat they pose in reality and I guess in a few times actually kind of throwing a bit of cold water on them. Debunking them to some extent or at least saying the risk is less than people might think, so it’s not all doom and gloom.

Robert Wiblin: Even though I know a lot about these topics, or at least a few of these, I still found that there was lots of fascinating little facts that I’m going to be throwing out in conversation over the next couple of years I imagine. Hopefully people won’t realize that I’m just cribbing from your book. So yeah, you’ve got this really beautiful summary table. There’s a bunch of nice figures and tables in the book, but maybe my favorite was this table 6.1, where you’ve just got this column which has got a list of all of the different risks and then ‘Toby’s best estimate’ of the chance of it causing a human extinction within the next hundred years and a couple of figures are, I guess… Yeah, asteroid or comet impact: there’s about one in a million chance in the next century. Super volcanic eruption: 1 in 10,000. We’ve got stellar explosion: so supernovae and something wacky like that would be one in a billion. But then we’ve got bigger risks that Toby thinks from anthropic risks. Like nuclear war is one in a thousand. Climate change is one in a thousand. Natural pandemics is 1 in 10,000. Engineered pandemics is a lot higher at 1 in 30. And we’ve got unaligned artificial intelligence which is way out there at 1 in 10. And then we’ve got kind of everything else, which I guess is about 1 in 30 or 1 in 20, which I guess then, if you add all these things together, it comes to a total chance of us not making it through this century of one in six, which is an interesting, potentially alarming figure depending on what you thought before. Yeah. Do you want to talk through the one in six figure? How much would you stand by that? How seriously should people take that?

Toby Ord: Sure. So with all of these numbers I should say that, when I go through the risks in detail and the science behind them, I try to give the scientific numbers. The numbers you can stand by. So, for example, the risk that the asteroid experts say is the probability of the Earth being hit by an asteroid greater than 10 kilometers across within the next hundred years. These types of numbers. But then there’s often a lot of uncertainty about what actually would happen if we’re hit by an asteroid of that scale or if one was detected, would we be able to work out some way of deflecting it and could we survive? What if we stockpiled food? What if we did this and that? And so there’s a lot of uncertainty that comes in for all of them. Even something as well characterized as asteroid risk. So all of the numbers that I give in this table, is a bit where I’ve tried to kind of cordon off my own subjective estimates of these things, but I felt that it would be almost irresponsible of me to write an entire book about this and to only talk about what I think about it in just qualitative times. To say, “I think this is a serious or severe risk” without actually explaining, “Do I think that’s a one in a million risk that’s still worth taking really seriously”? Maybe like the risk that you die on the way to the shops in your car and the reason that you put on a seatbelt and take actions to avoid that risk. Or is it a risk that’s much higher? So I tried to give these order of magnitude estimates as to how much risk there is I think from these different areas. But it’s not necessarily the case that if you read the book that I feel that you’ll be compelled to these numbers. It’s not that I think that they’re an accurate summary of the two pages I spent explaining a risk that it would force you to this number, but rather I figured that the reader probably wants to know what I think about these things.

Toby Ord: So the one in six risk, in particular. Yeah, I think that this is my best guess as to the chance that humanity fails to make it through this century with our potential intact. So either because we’ve gone extinct or because there’s been some kind of irrevocable collapse of civilization or something similar. Or, in the case of climate change, where the effects are very delayed that we’re past the point of no return or something like that. So the idea is that we should focus on the time of action and the time when you can do something about it rather than the time when the particular event happens.

Arden Koehler: So the time of no return would be something like warming or climate change has gotten so bad that even if it doesn’t cause us to go extinct now, it might in the next few centuries or it’ll cause the collapse of civilization and we won’t recover or something like that.

Toby Ord: That’s the rough idea.

Arden Koehler: Okay.

Toby Ord: And you can think of that, say, in the case of an asteroid as a nice clear example. That it would be the last time where you could have launched a deflection program or the last time when if you’d started saving and stockpiling food, that there would have been enough or that you could launch a program to develop food substitutes or whatever the thing is. But that’s often the critical time and actually, on my definition of existential risk, that’s when the existential catastrophe happens. The point where we lose our potential rather than the point where people are killed or something else. And so one in six is my best guess as to the chance this happens. That’s not a business as usual estimate. Whereas I think often people are assuming that estimates like this are, if we just carry on as we are, what’s the chance that something will happen?

Toby Ord: My best guess for that is actually about one in three this century. If we carry on mostly ignoring these risks with humanity’s escalating power during the century and some of these threats being very serious. But I think that there’s a good chance that we will rise to these challenges and do something about them. So you could think of my overall estimate as being something like Russian roulette, but my initial business as usual estimate being there’s something like two bullets in the chamber of the gun, but then we’ll probably remove one and that if we really got our act together, we could basically remove both of them. And so, in some sense, maybe the headline figure should be one in three being the difference between the business as usual risk and how much of that we could eliminate if we really got our act together.

Arden Koehler: Okay. So business as usual means doing what we are approximately doing now extrapolated into the future but we don’t put much more effort into it as opposed to doing nothing at all?

Toby Ord: That’s right, and it turns out to be quite hard to define business as usual. That’s the reason why, for my key estimate, that I make it… In some sense, it’s difficult to define estimates where they take into account whether or not people follow the advice that you’re giving; that introduces its own challenges. But at least that’s just what a probability normally means. It means that your best guess of the chance something happens, whereas a best guess that something happens conditional upon certain trends either staying at the same level or continuing on the same trajectory or something is just quite a bit more unclear as to what you’re even talking about.

Arden Koehler: Yeah, and I think we can get into some more detail about this later or more specifics later, but I am curious… Okay, so you think basically because of efforts that people will make to reduce risk, we will approximately halve it from what it would be if we had just followed business as usual. What kind of efforts are you imagining and why do you think we’re going to make that kind of effort?

Toby Ord: Sure. I think that if you take the two risks that I think are the highest, which are risks from unaligned artificial intelligence and risk from engineered pandemics. And I think that in both cases, as these technologies get more mature: these are not things that I think are going to happen next year. I don’t really think that they kind of could happen next year, but I think that they could well happen over the next hundred years. And as the technologies get closer and we see signs that are impossible to ignore about the power of these technologies and that there are certain kinds of near miss events where we really witness the power of an uncontrolled controlled version of this thing, that these are probably going to wake us up to some of these things. And even before that, hopefully the world will get woken up to these things by people in this community concerned about these risks.

Toby Ord: And I think that the arguments are actually both strong in a scientific sense and also very compelling if they’re done right. So I really do think that everyone can take these ideas seriously. Historically, in the existential risk community and within effective altruism, existential risk is often talked about in a fairly nerdy kind of way, a very ‘mathsy’… Very much if you think about the two cultures of science and humanities, very much in the sciences culture. Talking about things like, you know, maybe even if there’s only a one in 10 to the power of 20 chance of existential risk, you know, if it saves an expected 10 to the power of 15 lives or something like this. But I don’t think that one needs talk about it like that. And I think that you really can make a compelling case to everyone that the potential destruction of everything that they value, of all cultural traditions that they’ve ever strived to protect, and every bit of potential for all the good that they could create in the future, that the destruction of this would be bad and obviously bad and also quite compelling. And so I think that when that’s all realized, if I’m right that these risks are large at all, then that will become more obvious and people will react.

Arden Koehler: It seems like this book is an attempt to help that process along. You use a lot of sort of moving and even sort of lyrical language to try to really make vivid what’s at stake.

Asteroids and comets [00:16:52]
Robert Wiblin: Yeah, so I guess you open the section on the specific risks talking about asteroids and comets. I guess because it’s one of the ones that’s characterized. I don’t think we’ve actually mentioned them basically at all on the show in the 70 or so episodes that we’ve had so far. What is the threat and how’s the likelihood figured out here?

Toby Ord: Well astronomers divide up the risk from asteroids based on the size of the asteroid. There are those that are greater than 10 kilometers across, which is about the size of the one that killed the dinosaurs. They’re considered extinction threats, although it’s still a bit unclear about what the actual probability of extinction would be were we hit by one. But that’s one size category and they think there are four of those that are near-Earth orbits and that we’ve found them all. They’re not a hundred percent sure they’ve found them all, but it’s been a long time since we last found one and we can scan most of the sky and they should be relatively easy to see. There are also asteroids that are between one and 10 kilometers across which they think could cause some kind of severe global catastrophe. Maybe the ones towards the higher end of that range could cause an existential catastrophe and they think that there are about 920 and they’ve found about 95% of them and they work out how many they haven’t found by looking at when they detect another one, what’s happening to the rate of new detections over time and so on. And then the risk from that ends up being that there’s about a one in a one and a half million chance in an average century of being hit by one that is 10 kilometers across. But in the next century, it’s much lower than that because we have detected them and we’ve basically plotted the trajectories and they’re not going to hit us in the next century. So the risk is a hundredth of that at best.

Robert Wiblin: Yeah. Interesting. Okay, so asteroids we’ve kind of understood. We scan the sky. We’ve found most of them. Or at least we think we’ve found the big ones. What’s the deal with comets? Because they go much further out. They have weird orbits. Are they harder to see? Is that right?

Toby Ord: Yeah, I would say a lot of things are worse with comets. The standard thing that NASA will tell you is that comets are about a hundred times less likely to hit us. That is true. But it turns out that there are relatively more bigger comets and fewer smaller comets. So that there’s a different power law that they’re characterized by. And so when you’re looking at the very biggest comets, say the ones that are 10 kilometers across, the raw probability is actually similar to the asteroids. But then they’re worse in a number of other ways. They’re often traveling faster relative to the Earth which, if you know, non-relativistic kinetic energy is E = mv^2/2, and so the velocity makes a big difference and they’re also harder to detect and harder to deflect because they basically come on these really elliptical orbits where they’re just coming straight at us from the distant reaches of the solar system, and we’d have to intercept them and do something about them while they’re diving straight towards us. So there’s a lot of challenges with them. And astronomers were right to focus on asteroids first because they are a bit more common even at kind of relatively big ranges. But I think that now they’ve done such good work on the asteroids, that maybe it’s more important to actually start characterizing the comets.

Robert Wiblin: And I guess that involves looking out into deeper space and getting good at finding these dim objects?

Toby Ord: Yeah, I mean I don’t really know exactly what they should do. It’s not that I have some simple advice to them to say, “No, no. Switch your telescopes to look at a different point in the sky”! There are certainly big challenges, and they might need radically new techniques in order to deal with it, so I would suggest that they should devote some time to blue-sky thinking about are there really different approaches that would actually let them detect these things? If everything depended upon stopping one of these things, sure it looks difficult, but are there any kind of novel ways that we could understand them better or try to do that?

Robert Wiblin: Yeah. So I guess we haven’t completely fixed the comet problem, but on asteroids it sounds like this was actually one thing where we very quickly got our act together. Maybe because it was cheap enough that one country could basically take this on. Yeah. Do you want to talk about that? I was impressed by how quick was the thing from discovering that asteroids are a problem to actually just finding most of them.

Toby Ord: Yeah. I mean this was another big surprise for me when writing the book. The whole idea of asteroids is strikingly recent. So it was only in 1960 that it was scientifically confirmed that asteroids are what cause impact craters.

Robert Wiblin: What did they think before that?!

Arden Koehler: That’s crazy.

Robert Wiblin: It could be volcanoes?

Toby Ord: Yeah, so volcanoes also cause craters. And so they thought maybe it was some kind of geological activity that produced these things. There was debate about it. People had already thought that meteorites, these small rocks, that they fell from the sky. But they weren’t sure that there were big enough ones to create craters. They’d never been observed happening. And so in 1960, they confirmed that. Then in 1980, they worked out that they could cause mass extinctions with the Alvarez hypothesis by the father and son team. That that’s what caused the extinction of the dinosaurs. So that’s 1980; I was one year old when that research was done.

Arden Koehler: So before that they weren’t sure what caused the extinction of the dinosaurs?

Toby Ord: No, and while I was a kid, it took a while to filter down to the primary school level as well. It was an interesting hypothesis whereas it’s still not totally sure, but it’s looking quite a lot like a smoking gun. But yeah, it’s quite recent. And then after that, the community really got their act together and they approached Congress in the US and they had bipartisan support for it, for creating a spaceguard program. And then a couple of events happened, which really helped to cement public interest. There was the Shoemaker–Levy comet, the thing that crashed into Jupiter.

Robert Wiblin: Oh yeah, I think I remember that from my childhood!

Toby Ord: Yeah, exactly. And it left a mark, I think, the size of the Earth in the clouds of Jupiter.

Arden Koehler: That is poignant.

Toby Ord: Yeah, because they saw one of these things happen, it was in the news, people were thinking about it. And then a couple of films, you might remember, I think “Deep Impact” and “Armageddon” were actually the first asteroid films and they made quite a splash in the public consciousness. And then that coincided with getting the support and it stayed bipartisan and then they have fulfilled a lot of their mission. So it’s a real success story in navigating the political scene and getting the buy-in.

Arden Koehler: So that does seem strikingly successful compared to at least what I would guess is going to happen with many of the other existential risks that we’re going to talk about. How optimistic are you that at least for some of these others, we might be able to apply some of those lessons and have something similar happen?

Toby Ord: Yeah, I think not that optimistic.

Arden Koehler: What’s different about asteroids and comets?

Toby Ord: Yeah, I mean part of it, as I kind of suggested from that is that they got a bit lucky in terms of these films and the interest from that and this natural event with Shoemaker–Levy. It was, though, something that seemed very out there prior to that. Now those of us studying existential risk treat this at least as a fairly well understood example, a kind of poster child for something that people agree would cause an existential catastrophe if it happened. And that, you know, is less tendentious than some of these other types of arguments. But it’s still a pretty weird thing to be thinking about and they would have had to overcome those challenges. So there’s some hope from that.

Robert Wiblin: Are there any sort of asteroid deniers? I think that’s one benefit. The physical mechanism of a rock smashing into the Earth is sufficiently clear and indisputable that you can’t really have a movement that’s like, “No, we’re wasting our money discovering all the asteroids”.

Toby Ord: I guess that’s right.

Robert Wiblin: Yeah. I guess particularly compared to novel risks from AI or biotechnology that we’ll get to. It’s much easier to get everyone on board.

Arden Koehler: Although with bio at least and AI, it seems like there is a decent amount of media attention. There are movies that make them seem like existential risks. I think people don’t usually draw that sharp distinction between extinction and just very terrible, horrible catastrophe. But anyway, there’s at least some of that going on for some of these other risks.

Toby Ord: That’s right.

Supervolcanoes [00:24:27]
Arden Koehler: Yeah. So one thing that was surprising from the book for me was how high the risk is from supervolcanoes. So it seems like it was something like one in 200 this century and that seemed really high. It’s also a sharp risk because apparently we wouldn’t really be able to tell that it was coming, which makes it even more scary. So in all, it seems like maybe one of the most serious natural risks, but I don’t feel like people talk about it very much. So I was surprised by that. Why do you think people don’t talk about it very much?

Toby Ord: Yeah. Well there’s a few things going on there. So a supervolcano is, rather than a kind of cone towering above the Earth, it’s the type of volcano that’s so big that when it erupts, it produces more than 1000 cubic kilometers of molten rock that pours out of it. So that’s the threshold for being a supervolcanic eruption. So Yellowstone Caldera is like the most famous example of this. And the one in 200 is the chance of an eruption that counts as passing this threshold within the next century. But that probably wouldn’t kill us as evidenced by the fact that we have survived 2000 centuries so far, and so my overall number for the chance of existential risk from supervolcanic eruptions is about one in 10,000 over a century. As to why this isn’t more well known, I think that the real striking thing is the question, why is asteroids so well known? But they’ve both only really been discovered very recently. And there was a bit of controversy though, a while back, roughly 20 years ago I think to do with the Toba supervolcanic eruption, which was about 74,000 years ago, and it seemed to line up with a fingerprint in the human DNA evidence, which suggested that there was a genetic bottleneck at about the same time. So people thought that maybe humanity was nearly wiped out by this thing. But as people have looked into that more, it appears that the times don’t quite line up and people are more skeptical that it could have caused this kind of devastation. They do have a level where ash rains down on the scale of a continent and potentially on other continents as well is found from these things. They are very big. But it’s still unclear how they could cause our extinction.

Robert Wiblin: So they’d kind of produce a nuclear winter. So it’s a supervolcano winter and that’s the threat. That things start collapsing because there’s not enough food.

Toby Ord: Yeah, that’s right actually. And it’s interesting that you mention it. So the mechanism from supervolcanoes and from asteroids and from nuclear war… The main mechanism for causing existential risk is via a nuclear winter or volcanic winter or asteroid winter where particles get up into the stratosphere so high they can’t be rained out and then they cause global cooling: cooling, darkening and drying. But it’s the cooling that’s the main one because it shortens the growing season for crops. So that’s the main concern. And interestingly, for all three cases, it is a form of climate change and it is mediated by atmospheric science which is the subject that studies this. So if you look at the size of these asteroids, 10 kilometers is very big. It’s the size of a mountain. But it’s very small compared to the Earth. And the kind of image you might have in your mind if the asteroid ploughing into the Earth. It is more of a pinprick than two things of similar size.

Robert Wiblin: But so much dust.

Toby Ord: Yeah. But it is the dust. I guess these types of people who, you know, which would make them a climate denier, they could deny that there would be these dust effects and things. And in the case of nuclear winter, there was a lot of denying of this. There’s a lot of pushback that Carl Sagan and others received on the theory. Partly because it was a politicized issue somewhat like we’re seeing with climate change. So one could push back on supervolcanoes and asteroids for the same reason, but you don’t see that so much because it’s not politicized.

Arden Koehler: It’s interesting that so many different risks share this same mechanism. It suggests that one of our biggest vulnerabilities is our atmosphere, or our access to sunlight.

Toby Ord: Yeah. That’s right. And there’s a useful way of thinking about this, which is that once there’s some kind of event, is the event so big that it just would obviously destroy the Earth? For example, if an entire planet crashed into the Earth or something where it’d be pretty obvious how it gets big enough. But in other cases, there’s this question about how does it scale up to be something that could threaten us all? How does it get everywhere, like to all the humans and so on. In the case of all of these things, what happens is that the atmosphere is what takes a thousand kilometers of rock or square cubic kilometers of rock or what have you, and distributes it in such a way to create this opaque layer around the Earth. And without the atmosphere doing that, it would be more of a regional catastrophe. And then the atmosphere is also important in climate change and also temperature changes are also important there. And the effects of temperature change potentially on crops. So there’s actually quite similar things about some of these natural catastrophes and even some anthropogenic ones that are quite interesting.

Robert Wiblin: I wonder if the reason that supervolcanoes are less known is that it just makes for a worse plot of a movie. So I guess with an asteroid, you have this lovely property that you find it way before and you’ve got everyone freaks out and then you’ve got a story where you go and try to intercept it. But with a super volcano, in reality, it would happen like very unexpectedly and very suddenly. And so I guess it’s a survival movie, whereas you know, people are trying to minimize the number people who die in this disaster, but that’s less cool than going and like blowing it up.

Toby Ord: That could be right. Definitely the “Armageddon” versus “Deep Impact”. They went with the more machismo approach there. I guess when I think about it as a movie, maybe it would be interesting. You could probably make just as interesting a movie, there’s still something about the supervolcanic eruptions that seems faintly ridiculous to me, but I’m not sure that they are any more ridiculous than asteroids, or that it gives me any reason to doubt the science. But in terms of that aspect about, do things just seem too weird? It’s interesting that that’s an example where I still feel it’s weird. I have a little bit of trouble taking it seriously.

Arden Koehler: Can you tell which part of it is weird or that is making you feel like it’s just ridiculous? Or is it hard to say?

Toby Ord: I guess the name wasn’t great. Supervolcanoes sounds a bit comic book. And also, when you think of a volcano, you know, Vesuvius, and then destroying the whole world. Whereas if they just had a totally separate name, a different kind of geothermal activity that causes different kinds of destruction, maybe it would seem just a bit more normal and you’d think, “Oh, I guess that’s interesting”.

Arden Koehler: I’m curious why it would be hard to tell if a supervolcano was coming? It seems like, extremely naively, we do have access to the parts of the Earth that are going to be changing leading up to this, so why would it be so unexpected?

Toby Ord: I think the answer to that is mainly because it’s unprecedented. So, for example, suppose we discovered a sharp increase in geothermal activity at Yellowstone or something and our best kind of detectors showed that there were large amounts of magma moving under the surface and so on. Well then, what would we say about that? We don’t have a track record of correlations between large amounts of magma moving under there and how long it is or what the chance is that that then leads to it causing a supervolcanic eruption because we have witnessed zero of them. The information we do have is from the kind of debris that they’ve scattered by previous ones and finding the calderas and trying to investigate them, but we don’t have access to what were the precursor signs before that. So if we saw something really striking happening, maybe we’d think there’s at least a 10% chance something really bad’s going to happen over the next century. But maybe it would happen in one year or maybe it would happen in 70 years. And we’d have just very little idea about it. Whereas with asteroids, once we detect them, then it’s just high school physics to then calculate how long it will be before it hits the Earth.

Robert Wiblin: Yeah. So David Denkenberger in episode 50, he’s got a list as long as your arm of various engineering ideas, and the ones that we spoke about in the interview would be how would we feed people through a volcanic winter and he’s also got a bunch of like how would you stop a supervolcano from erupting if you thought it was going to, including just like building a mountain on top of it which apparently no one has really investigated in any depth to see whether that would work or whether it might just increase the risk because then you’re bottling up this thing and then it’s even worse. I suppose that’s something that governments could potentially fund, because I don’t think there’s been much work on this.

Toby Ord: Yeah, it’s an interesting question. One thing I’m worried about with it is the chance of making it worse, because just the baseline risk is very low, and we know it to be low from our survival. So it seems that if we then do something that may make it better or may make it worse, we’re starting from such a low level that I’m not sure that we’d want to be taking those risks.

Robert Wiblin: Yeah, so if it was a one in 200 chance of making it worse or something like that.

Toby Ord: Yeah, then maybe I’d probably be pretty happy about it. But yeah, you see the problem there, as well as the political risks of… there could be an asymmetry between kind of acts and omissions in terms of the political ramifications of intervening in supervolcanoes.

Threats from space [00:33:06]
Robert Wiblin: Yeah, that makes sense. All right, so another one that you go into, which I knew very little about, is threats from space. So we’ve got supernovae and things like that. What things can come at us from space and why do we think it’s basically a negligible risk in practice?

Toby Ord: Yeah, so sometimes stars explode. Supernovae: we’ve known about those for a very long time when Chinese astronomers catalogued a new star appearing in the sky. But it’s only quite recently in the last hundred years that we’ve realized that this could actually be a risk to humans if it happens close enough. The idea is that the radiation from this would cause chemical reactions in the atmosphere, which would produce nitrogen oxides, which would then severely damage the ozone layer, which would cause extra UV exposure. That’s their kind of best known mechanism. But extra UV exposure–

Robert Wiblin: Doesn’t sound that bad.

Toby Ord: It doesn’t sound that bad. Supernova sounded really bad.

Robert Wiblin: Just stay indoors!

Toby Ord: But supernovae happening many light years away is the actual case. We’re not talking about our sun turning into a supernova. That then starts to sound less clearly bad and then the mechanism doesn’t sound that bad again. Yes, like what about shielding and so on? Stay indoors, maybe you need to wear protective suits to do farming or something. And, at the moment actually, most farming is done by automated tractors, kind of under GPS and so on that just work night and day and don’t have humans out there.

Arden Koehler: They don’t have humans in tractors anymore?

Toby Ord: At least I think not in the UK and the US.

Arden Koehler: I didn’t know that.

Toby Ord: Yeah, they can work all night as well because they don’t need to see. So I think that the probability of this happening is very low and the mechanism doesn’t sound that plausible and the risk would be that as a supernova, not like any star out of the 100 billion in the Milky Way, but any star within about 30 light years, maybe say one of the closest thousand stars turning supernova. And none of them look like they’re in a process where they’re nearing the stage of their life where they might do that. The other kind of risk that you were alluding to is that of gamma ray bursts. And that’s a thing that was only just discovered very recently. In the cold war, the Americans developed satellites to detect the gamma ray flash of a nuclear test to see if there are other countries, particularly the Soviet union, who were doing nuclear tests. And then they found their detectors going off a lot and they tried to work out what was happening, and they realized that it couldn’t possibly be coming from the Earth and they discovered these gamma ray bursts, which were happening from other galaxies, and the radiation was so intense that we could detect it here, including, I think there was a case of it happening billions of light years away that was detected.

Toby Ord: So a gamma ray burst can be triggered by either a rare type of supernova or two neutron stars crashing into each other. So fairly exotic phenomena that doesn’t happen very often but can be felt a long way away. And basically, very roughly, it’s about the same amount of energy released as in a supernova, but instead of being released, spherically symmetrically, it’s released in these two cones at the poles. And so it could reach much further because it’d kind of be more intensely concentrated, so it could reach from other galaxies. Well detected from other galaxies. It couldn’t kill you from other galaxies. I looked into it in some detail, and there was a lot of concern about this cone angle business, that if the angle’s very narrow, then it could get you from very far away.

Toby Ord: But it turns out if you actually do the maths on it, the volume that it irradiates at a lethal dose is exactly the same regardless of the cone angle. It’s just a narrow thin thing versus a thick wide thing. And so it’s a bit of a red herring, I think. And it ends up irradiating a similar volume to that of the supernova, which is not that large a region and therefore is extremely unlikely and it’s unlikely to cause an extinction event in the whole time that the Earth will be habitable.

Estimating total natural risk [00:36:34]
Arden Koehler: So abstracting a little bit away from these particular natural risks, you also have a way of estimating the total natural risk. Do you want to just tell us a little bit about what that is?

Toby Ord: Sure. The basic idea is like this. We have this catalog of risks that we’ve been building up: these things that we have found that could threaten us. A lot of which we just found in the last hundred years. So you might think, “Well, hang on, what’s the chance we’re going to find a whole lot more of those this century or next century”? Maybe the chance is pretty reasonable. If you plotted these, which maybe some enterprising EA should do, over time and when they were discovered to see if it looks like we’re running out of them. I don’t think that there are particular signs that we are, but there is an argument that can actually deal with all of them, including ones that we haven’t yet discovered or thought about, which is that we’ve been around for about 2000 centuries: homosapiens. Longer, if you think about the homo genus. And, suppose the existential risk per century were 1%. Well, what’s the chance that you would get through 2000 centuries of 1% risk? It turns out to be really low because of how exponentials work and you have almost no chance of surviving that. So this gives us a kind of argument that the risk from natural causes, assuming it hasn’t been increasing over time, that this risk must be quite low. In the book I go through a bit more about this and there’s a paper out that I wrote with Andrew Snyder-Beattie, where we go into a whole lot of mathematical detail on this. But, basically speaking, with 2000 centuries of track record, the chance ends up being something less than one in 2000 is what we can kind of learn from that. And this applies to the natural risks.

Arden Koehler: So the basic idea is nothing’s really changed when it comes to supervolcanoes or asteroids in the last 2000 centuries. So if we’ve survived this long, we shouldn’t expect to have anything approximately above a one in 2000 chance of witnessing something like that this century.

Toby Ord: That’s right. If anything’s changed, it’s that we’re more robust against them.

Arden Koehler: Yeah, so at most.

Toby Ord: We spent about 130,000 years over the last 200,000 in Africa. So just being a one continent. If there was something that could have changed the climate of a continent, maybe we would have been vulnerable. Now we’re spread across many continents. We have many more different types of crops that we use and many new technologies and so on that seems to make us more robust. So if anything, it seems like the chances are decreasing. We’re becoming less vulnerable to it.

Robert Wiblin: Yeah. You write in the book that this doesn’t fall foul of the anthropic concern that if we’d been wiped out by one of these things, then we wouldn’t be around to see it and make these estimates. But I’m not sure I completely understood why there’s not a big adjustment from that.

Toby Ord: Yeah. So I think what you’re getting at there is that someone might say, “Well, the chance can’t be that high or we wouldn’t be here”. And then you can say, “Well hang on a second. If you imagine that there were a whole lot of different planets and maybe the chance was high, while the only survivors would be on the planets that happened to get lucky, so this argument would be misleading them”. Maybe our Universe like that, but is that the kind of thing–

Arden Koehler: We’re the lucky ones.

Robert Wiblin: Yeah. So you can imagine that you start with thousands of planets with humans on them. And then no matter what the risk is, there’s always the people on the remaining ones going, “Well, the risk is really low”! And then like 99% of them get wiped out every time.

Toby Ord: That’s right. So here’s the kind of thinking, though. And Nick Bostrom and Max Tegmark have a great paper on this where they were looking at the risk of vacuum collapse, which is a risk that I only touch on for about a sentence in the book, where the idea is that is there some chance that the vacuum in our universe is not the lowest energy vacuum and that it could decay to the lowest energy vacuum producing an explosion that would travel out at the speed of light changing all of the vacuum to this new thing creating huge amounts of energy.

Robert Wiblin: I really feel like I should google this and figure out what the hell people are talking about when they talk about vacuum collapse. Yeah, anyway, we shouldn’t get distracted by that.

Toby Ord: Well, if you’re thinking that the issue is that if there’s nothing, how can it collapse–

Robert Wiblin: Right, how does nothing collapse?

Toby Ord: Well, the idea is that the vacuum is not nothing. It’s a low energy state, but not the lowest energy state and so there is some amount of energy that can go down further.

Robert Wiblin: But if a little bit of it goes to the lower level of energy, why does that create an explosion of lower energy? Maybe we need a physicist.

Toby Ord: Yeah, you might want a physicist. The idea is meant to be like a crystal in a supersaturated solution where when you have this–

Arden Koehler: All clear to me now!

Toby Ord: Yeah, let’s leave it there…

Robert Wiblin: Yeah. Alright, that was a diversion. You were saying that there’s this paper about it.

Toby Ord: Yeah, there’s this paper about it, and you can say, “Well, what is the chance of this risk? Maybe it could be really high and we wouldn’t know because we’d still see ourselves here”? But then the idea is, well hang on a second, if it was high, we are 13.8 billion years into the Universe’s time period. There have been planets that have formed much earlier than the Earth and suppose the risk you were saying could be as high as 50% per century. Then you could say, “Well, couldn’t humanity have just evolved in a million years less? Like, you know, just 0.1% faster of the evolution of life on Earth. How unlikely would that have been? And it would have saved us 10 centuries, which is a factor of a thousand in the probability. So you end up kind of saying that we basically would find ourselves at the earliest possible time that we could find ourselves in those cases.

Arden Koehler: I don’t understand. We should find ourselves at the earliest possible time. But here we are and it’s not the earliest possible time. How do we know that?

Toby Ord: Oh, so we don’t just know that from that. We would need to notice, for example, that there were planets that seem to be just as habitable as the Earth which formed a billion years earlier, for example. And the reason why we know we will be astronomically more likely to find ourselves on such a planet than on this planet that happened to just get lucky for an extra 10 million centuries of risk.

Arden Koehler: I see! So this is evidence against the idea that there are tons of possibilities for humanity to evolve, and we’re just the lucky ones. It actually looks like there weren’t tons of possibilities, so then it would be astronomically unlikely for us to get lucky anyway.

Toby Ord: That’s basically right. And the idea is that you could run a somewhat similar argument to do with how long we’ve been around. That there’ll be almost no one discussing this question. I mean how many planets would there have to be before there were people who managed to get 2000 centuries further on and are having this discussion. Almost all the people who kind of were wondering about this would be much earlier in the history of their species. Anyway, this is where it’s trying to make the disanalogy is that this number of how long we’ve survived so far is the thing that’s supposed to be breaking out of that anthropic situation where we couldn’t say anything about the probability of events where we could only witness being alive because we could witness different lengths of survival time. And so that’s where the information’s is coming from.

Arden Koehler: But surely if we’d survived much shorter than we actually had, we wouldn’t have had time to get smart enough to ask these questions?

Toby Ord: That is where some complications come in and it’s to do with reference classes and things which are very confusing bits of anthropics. I would say that anthropics is such a complicated thing, generally. I don’t rely on it at all in the book. As in, I don’t make any arguments that actively make use of it. But I may be vulnerable to, if certain theories of anthropics turn to be true, then that creates challenges to some of the things I say in the book.

Arden Koehler: Okay, well somebody should go away and figure this out.

Robert Wiblin: I think I get it, but I’ll see if I can find a blog post level explanation of this for myself and listeners and stick up a link to that in the show notes.

Arden Koehler: So you make use of the fact that there are all these figures on what are typical lifespans for species. But it seems like the typical lifespan of a species actually varies a lot and so you give some examples of that. Horseshoe crab has a lineage of 450 million years. The Nautilus, 500 million. Sponges, 580 million. These are all very tiny, simple species. We are not like that. Is there some, I don’t know anything about this, but is there some pattern that suggests that these tiny, simple species are often much more long-lived and that the natural extinction rate of bigger, more complex species is higher?

Toby Ord: That’s a good question. I don’t know what the overall relationship is there. One of the issues that’s a confounder is that most species are much smaller than us. At least most animal species. We’re actually very large animals. We fixate on the ones that are bigger than us, like elephants and tigers and things. But there are a very small number of elephants and tigers and things and a very small number of such species as well. So most species are small species. Therefore one would expect most of the long-lived forms to be small as well. And it’s hard to factor out that. But there’s also the question about being marine species has made them much safer from some of these natural catastrophes as well.

Robert Wiblin: Also, I think all of these are like at the bottom of the ocean as well, which might be an even more stable environment.

Toby Ord: Yeah, that makes a lot of sense. But I think that they do point the way to what might be possible. If we can protect ourselves from threats to the same degree to which, say, these marine species can protect themselves from threats, create safe environments for ourselves and so on. Then there’s kind of no reason that we couldn’t last for hundreds of millions of years.

Arden Koehler: So this kind of suggests an upper bound or not even an upper bound, but just showing like, “Hey, the horseshoe crab did it”.

Toby Ord: Exactly.

Arden Koehler: And we can too.

Toby Ord: It’s a kind of proof of concept thing. That’s the kind of bar for what we might hope to achieve. I think that we’re often quite unambitious in our hopes for the future and trying to exceed what the horseshoe crab did could be a lower bound on our ambitions for the future.

Robert Wiblin: All right, we’ll return to that in our vision for utopias.

Arden Koehler: You should’ve put a horseshoe crab on the cover of the book. I feel like that would’ve been cool.

Robert Wiblin: Yeah, I like that symbol. Yeah. Maybe we should respect the elephants less and the sponge more.

Distinction between natural and anthropogenic risks [00:45:42]
Arden Koehler: I want to just introduce the distinction between the natural and anthropogenic risks and why you feel like this is such an important distinction. So you talk about the fact that we’ve been around for 2000 centuries as a big source of evidence that these natural risks are pretty low. Maybe bracketing some anthropic considerations, but you think that basically doesn’t give us any evidence or maybe it only gives us a little bit of evidence when we’re thinking about how vulnerable we’re likely to be to risks that are caused by human action. And that feels like a really important line of argument in the book. So I thought you could just talk about it and talk about why you’re so convinced by that.

Toby Ord: That’s right. This doesn’t show that the anthropogenic risks are high, but you might’ve started with some kind of prior probability distribution over how likely it is that we go extinct from various different causes. Perhaps you were thinking about asteroids and how big they were and how violent the impacts would be and think, “Well, that seems a very plausible way we could go extinct”. But then, once you update on the fact that we’ve lasted 2000 centuries without being hit by an asteroid or anything like that, that lowers the probability of those, whereas we don’t have a similar way of lowering the probabilities from other things, from just what they might appear to be at at first glance. So that’s not to say that they are high, but that they don’t have this nice reassuring way of making sure that they are low. There are separate arguments that perhaps suggest that they’re high.

Toby Ord: And that one important kind of exception is pandemics, which I imagine we’ll come to later. But there’s something where there are plausible stories about how what we think of as natural pandemics are actually closely interlinked with human activity, both that we might be at higher risk of initiating them and that if they did happen, we’d be able to spread them around more because we’re more interconnected than we’ve been in the past. So this is a rare case of something that we’d often think of as a natural risk, but is something that the way the risk has been plausibly increasing over time, so we can’t help ourselves to this argument in that case either. And so for that reason, I don’t categorize them as a natural risk. And I think that’s actually just a useful way of making that division. It’s always hard to make the division between the natural and the artificial because everything’s natural. At some level. We are natural too as humans. And this is actually therefore a convenient place to draw that line as to the ones that we’ve got this kind of safe argument for.

Arden Koehler: So do you think that something like “natural pandemics”… Can we use the fact that we have survived for 2000 centuries at all when thinking about how likely they are to wipe us out or not at all? It’s somewhere in between?

Toby Ord: Yeah, I think it’s interesting. I hadn’t thought about this much actually while writing the book until you mentioned it, but we can kind of use something about this fact that we survived the natural risks to suggest that the risk from anthropogenic things might be a bit lower than you would naturally think because some of the mechanisms whereby we survived these other things might suggest that we’re more resilient than you might’ve thought at first glance. Whereas it also could just mean that the initiating events, such as the number of asteroids that collide into the Earth is low. That wouldn’t help us feel safe about future things. But also, some of the reason could be to do with resilience and so that would actually help us feel a little bit safer.

Arden Koehler: Yeah, I guess maybe there have been climate events that we have survived, which might give us some evidence about how likely we are to survive through climate events that are caused by people.

Toby Ord: Yeah, that’s a good example. So we’re getting more into the particulars than merely the fact that we’ve been around for 2000 centuries. But we’ve been through some quite dramatic climate events. We have lived through a glacial period and interglacial periods. And so we came out of a glacial period around about the time when agriculture started about 12,000 years ago. So that was a time when there was radical change to the Earth and the environments across the globe. But actually it turned out to be very good coming out of that and seemed to be a precursor to allowing us to have civilization. And that’s not the only kind of glacial-interglacial change that we’ve been through. So you could kind of read something into that about the levels of temperature change that we’ve had that’s between the current level and colder, not the current level and hotter.

Robert Wiblin: I guess another thing that I find generally reassuring is that when I look inside my internal model of the world, in my mind, I feel like just the wheel should be coming off all the time and there should be tons of midsize disasters that kill millions of people, but this just doesn’t seem to happen nearly as much as I would predict, which means that my model is kind of missing something. Perhaps I’m just missing how much effort people put into preventing disasters or how good they are at predicting them and seeing them off.

Toby Ord: I think that’s a very good point. One often thinks, “Well, you know, what would stop someone doing this heinous thing”? And you realize, “Oh my God, there’s almost nothing to stop someone doing that”, and then you think about the track record and it seems to show you something about the rate at which people are actually motivated to do that terrible thing. And there’s something important there that you’re learning or perhaps that they’re stopped, or nipped in the bud, or things like the way that moral education for people in schools and things is kind of stopping people from having those ideas or it’s detecting them early on. So there are indeed some reassurances we can get from that. But things change, as we might get to, when it comes to biorisk. If the tools to do something terrible increase so that a thousand times as many or a million times as many people have them available, then it might be that the historical track record is only a rather small number of people who could done this terrible thing. And if you then think, “Oh, now we’re going to get a hundred times as many people having the ability as have ever had the ability before”, the historical track record tells you very little about what would happen there.

Robert Wiblin: Yeah. I guess it also might change the psychological stability level that you need to get to in order to have access to these weird technologies. Again, as much as you have to be a professor to get access to it. Maybe you’ve gone through a bunch of filters in the first place.

Toby Ord: Yeah, that’s a good point.

Climate change [00:51:08]
Robert Wiblin: Let’s push on and talk about climate change. This is one where you said you’d changed your mind a whole bunch and I suppose my background assumption on this… My guess has been, well, climate change is going to be really bad, but surely it can’t drive us extinct. Surely it’s not going to actually end civilization. People are exaggerating when they say that. I’m really glad that you’ve actually put in some time to look into this and try to form a view. Yeah, what did you learn?

Toby Ord: Yeah, it’s complicated. I’ll give you a whole lot of reasons that you should be more concerned and also reasons you should be less concerned. How they all balance out is a bit unclear, but I’ll treat you to some interesting observations on it. So, when I first looked into it, one thing I wanted to be able to say when writing a section on it is, well, some people talk about the Earth becoming like Venus. So having this runaway climate change where the oceans start evaporating, creating more and more water vapor in the air and that this can run to completion and basically we’d have no oceans and the temperature goes up by hundreds of degrees and all life ends. Or at least all complex life. So I wanted to be able to at least say, “Don’t have to worry about that”.

Toby Ord: It turns out that there is a good Nature paper saying that that can’t happen no matter how much CO2 is released. You’d need brightening of the sun, or to be closer to the sun for it to happen at any CO2 level. But normally one Nature paper saying something, you know that’s enough to say, “Yeah, probably true”. But there’s a limit to how much epistemic warrant can be created by a single Nature paper on something. But it still seems like that probably isn’t going to happen and no one’s really suggesting it is going to happen. There’s another thing that was a bit alarming there with something called a ‘moist greenhouse effect’, which is similar, but doesn’t go quite as far, but you could still get something like 40 degrees Celsius extra temperature. And the scientists are like, “Oh yeah, I mean you can’t get this runaway, but you might be able to get this moist one”. And from a lay person’s perspective, you think, “Well hang on a second, why didn’t you include that in the other category? I thought when you were giving reassurance as the other thing wasn’t possible, that you weren’t saying there’s a thing that’s, for all intents and purposes, identical, which is perhaps possible. And that one also probably can’t happen, but people are less sure and there are some models that suggest maybe it can.

Arden Koehler: So when you say for all intents and purposes it’s similar, you’re thinking because 40 degrees warming would be all but guaranteed to wipe everyone out?

Toby Ord: Yeah, I guess to the extent to which even a hundred degrees of warming is. You know, maybe we could build giant refrigerated areas where some people could survive and so on and we could come back. If you think about saying the chance that we could set up a permanent base on Mars or maybe a permanent base on Venus–

Robert Wiblin: Antarctica, maybe?

Toby Ord: Yeah, Antarctica. It doesn’t seem implausible that we could do such things, say in the next hundred years. And so maybe it’s not implausible that we could also, if with a smaller population, kind of weather such an event. But it’s looking pretty bad and there wouldn’t be much of a discussion about, “Is that an existential risk or not”, if we thought that was still happening. So to be clear, I don’t think either of those things are going to happen, but I have found myself, unfortunately, not being able to rule it out to any kind of particularly strong degree of confidence. That’s the first bit.

Robert Wiblin: Don’t they fall foul… I mean, the Earth’s been around for billions of years. The temperature’s gone up and down. It’s been, I think, quite a bit hotter at some points than it is today. And yet, you know, the oceans didn’t boil away.

Toby Ord: Yeah, it’s been much hotter. And this was the line of evidence that I was hoping to use to settle the issue on this in order to then delineate the part of conversation that needed to happen to say, “Don’t worry about those things that you might’ve heard. Worry about these other things and then here’s how they could work”. But unfortunately, this so-called ‘paleoclimate’ data about the long distant past and what the climate was like, it is not that reliable. And also the Earth was different in many ways when these things happened. For example, sometimes when you had these different temperatures, there was a supercontinent instead of the current situation where the continents are all divided up and these caused very different effects in the atmosphere and so on. So the paleoclimate data, you couldn’t just make that kind of assumption that, “Hey, it’s been way higher than this in the past, therefore if it goes way higher it’s not going to cause this problem”. And also, there’s a lot of concern that the rate is important as well as the level of the temperature. And that’s something where the rate of warming at the moment, I think, could well be unprecedented in the history of the Earth. Again, the evidence isn’t great on that because if you think about the temporal resolution that we have, we’re only really measuring the temperature at kind of times many thousands of years apart.

Toby Ord: So it’s hard for us to know if it was actually very spiky in the intervening periods. But it’s at least quite plausible that even though it’s not plausible that this is the hottest that the Earth’s ever been, it is plausible that it is the highest rate of warming and also that that could precipitate serious problems. So unfortunately the paleoclimate data while somewhat reassuring is not as reassuring as I’d hoped going into this book.

Robert Wiblin: It’s not dispositive. Okay. So do you want to carry on with the other ways that things go really badly?

Toby Ord: Yeah. So there are various feedback effects that can happen where warming creates more warming. I should say that these are the amplifying feedbacks. There’s also stabilizing feedbacks, where more CO2 release actually then creates more of a sink for CO2. So it’s complicated. There are both kinds of feedbacks. And there are certain effects though which could produce very large effects. So I’ve focused on the ones in the book as to what could do the biggest things? And so the two that I focus on in particular, are the permafrost and the methane clathrates. And so these are two kind of big stores of carbon. One is in the tundra and I think also under the sea: the permafrost. And the other is methane clathrates: an ice-like substance at the bottom of the ocean floor.

Robert Wiblin: That’s full of methane?

Toby Ord: Yeah, that’s right. And both of them contain far more carbon than all emissions so far and in fact more carbon than the entire biosphere. So if they were completely released, we could get very severe warming, much more than from all of our fossil fuel use. But, scientists think they’re probably not going to be all released or if so, it would be extremely gradual over many centuries and so forth. But it’s kind of hard to rule out. Like again, it would be nice to be able to say, “Oh, when you look at it, you find out that it’s still only a quarter as much as we’ve ever released or something like that”. That’s not the case. We can’t help ourselves to the kind of safety on that.

Robert Wiblin: Or we have this superstrong argument why it can’t happen. Why they can’t all melt. We just don’t.

Toby Ord: No we don’t. Scientists aren’t greatly alarmed. They’re not saying that that’s definitely going to happen precipitously or something. By the same stock it’s hard to put bounds on it.

Robert Wiblin: Do you have a sense of how much the world would warm if the methane clathrates just all started melting and the methane went up into the atmosphere?

Toby Ord: So it’s very hard to estimate these things because they go so far outside the known range for the models, but attempts to estimate a very similar thing of what would happen if we burned all known fossil fuel reserves, where they were looking at 5,000 gigatons of carbon, which is actually about the amount in the methane clathrates, suggested between nine and 13 degrees of warming.

Robert Wiblin: Okay, so quite a lot.

Toby Ord: Yeah, a really large amount.

Robert Wiblin: Yeah. I guess coming back from these more exotic scenarios to just the main line thing of what if we just keep burning a whole lot of fossil fuels. Yeah. How did your view shift on how likely that is to be a real disaster for civilization?

Toby Ord: Yeah. I think one of the key numbers here is this thing called the ‘climate sensitivity’. And this is the number that represents how much warming would there be if we doubled the amount of CO2 in the atmosphere. And it’s relatively easy to understand that if there were no feedback effects. However, when there are feedback effects, particularly some of them that are very hard to model, there’s a lot of uncertainty, and the current estimate is that if we doubled the CO2 emissions level, as in the level of CO2 in the atmosphere, that there would be between 1.5 and 4.5 degrees of warming. But unfortunately, this is a very big range and this is actually kind of wild amounts of uncertainty. So the high end is triple the low end and that’s not a 95% confidence interval. That is a two thirds confidence interval. So they’re saying that, “Well, you know, it could be one and a half degrees or it could be triple that”. And when you combine that with the uncertainty about how much we’re going to actually emit, how high the level is going to go. For example, if you think it could be between one and two doublings of pre-industrial amount of CO2 in the atmosphere, then you end up with an estimate of warming between one and a half and nine degrees, which is a extreme range of outcomes.

Arden Koehler: It does seem pretty plausible that we could end up emitting as much carbon in the atmosphere again and then again, especially over like all time because these things are cumulative.

Toby Ord: That’s right. And I don’t think that we are going to stay on the “business as usual trajectory” or something and just keep following this curve of exponential carbon emissions. But, you know, it’s not impossible. It’s a social science question. One where it’s impossible to kind of really be having 99% confidence in these things and so on. I can imagine scenarios where that could happen. Where, for example, there’s a new Cold War and it’s in one of the superpowers’ interests to just emit as much as possible and they just go for it.

Arden Koehler: Or even if the rate of emissions goes down but it continues to be positive, then it might just take longer but we could still see really substantial warming. Although of course if it takes longer, then we’ll have more time to adapt.

Toby Ord: Yeah, but I agree that we could have really substantial amounts of emissions.

Robert Wiblin: I think something that surprised me was just looking at, well we’ve got uncertainty about the emissions of maybe 2x, possibly 3x. Then we’ve got uncertainty within the model which is big, like 3x difference of the climate sensitivity. And then we’ve also got out of model uncertainty, which is like, “Well, what if our model of this is quite wrong? Then we should increase that even further”. Because yeah, there’s ways that we could be wrong that we haven’t even thought of yet, but they’re not included in this climate modeling. Then you’re like, “Well, I guess 12 degrees is not that inconceivable”. It could be massive. And in fact, the odds of it being over 6 degrees really isn’t that low. Not as low as I thought it was.

Toby Ord: That’s all right. And the most extreme number you hear is six degrees. And also it turns out when people say things such as, “We need to do this policy in order to keep warming below, say, three degrees”. What that typically translates into scientifically is in order to keep the median amount of warming below three degrees. But, if we’re wrong about climate sensitivity, it could be five degrees even if we do that policy. So these things are very uncertain, very wide distributions. So I was quite a bit more alarmed by that after looking into it about how little is known about this.

Robert Wiblin: Did your opinions change at all on how resilient we would be to these changes. I suppose at the moment it seems like human ingenuity is winning out. The climate’s heating, but we’re getting so much better at farming all the time that, you know, the amount of food output just keeps rising at a pretty good clip. So is it possible that we will just be able to adapt to this because it’s happening over decades?

Toby Ord: I think so. It would still be much worse than if it wasn’t happening. Just to be clear on that for the audience.

Robert Wiblin: We’re talking here about like would we all die? Would it cause the collapse of civilization, which is a high bar.

Toby Ord: That’s right, it’s an extremely high bar. And while there are a lot of things which could very clearly cause a very large amount of human misery and damage, it’s quite unclear how it could cause the extinction of humanity or some kind of irrevocable collapse of civilization. I just don’t know of any effect that could plausibly cause that. There has been some analysis of if you had very large amounts of warming, such as 10 degrees of warming, would it start to make areas of the world uninhabitable? And it looks like the answer is yes. At least being outside, air conditioning could still work. It’d still be much more habitable, say, than Mars. People are perhaps thinking of setting up settlements. But also that argument though, if you run it through, it really just suggests that the habitable part of the world would be smaller. So coastal areas are much less effected. High plateaus such as Tibet wouldn’t be moved to super hot temperatures. So there would still be many places one could be. It would be a smaller world. And it seems hard for me to think that given it wouldn’t be that much smaller, as to why then civilization would be impossible, or a flourishing future would be impossible in such a world. That just doesn’t seem to have much to back it up at all.

Arden Koehler: So even if it was a third of the size, then one might think–

Toby Ord: I mean if we heard that someone had found a planet in the habitable zone around a nearby star, but it had a lot of ocean and only had a third of the land mass of the Earth, we wouldn’t think, “Oh, well I guess no need to worry about ever meeting anyone from that planet, because it’s impossible to create a civilization on such a planet”. Or, say, it was only the Americas and you didn’t have Africa or Eurasia or Australia that, oh obviously, you never could have had civilization there or you could never sustain it. That would seem kind of like a pretty crazy view. So I don’t really buy the idea that large enough parts of the Earth could be made uninhabitable either.

Arden Koehler: Well at degrees of warming like 10 or whatever, but if we get up really high, I mean, it seems like it’s not–

Toby Ord: Yeah, I looked at these models up to about 20 degrees of warming, and it still seems like there would be substantial habitable areas. But, it’s something where it’d be very bad, just to be clear to the audience.

Robert Wiblin: Most people are dying.

Toby Ord: Yeah, it’d be very bad. But it’s hard to see any particular mechanism that’s being floated as to how it would happen on model. But my concern is more than just the prior probability. Before you even got into these models or got into the science of it, if we make an unprecedented change to the Earth’s climate, perhaps at a truly unprecedented rate over the last 4 billion years, and also to a level which has only a couple of times been reached or something and never been reached with the current configuration of continents or with a species like us and so on, that it does seem like there’s just some plausible chance that this is the end. It’s not that if you imagine kind of appearing before Saint Peter at the pearly gates and he said, “Hey, yes it was climate change” and you’re like, “How could we have possibly known that making these radical changes to the Earth’s climate that haven’t been seen for millions of years could do us in”. I think we’d be looking pretty foolish. It does seem like even if we said, “But our scientists looked at these different pathways and none of them could lead to it”. And you’d think, “Well, it could have been one that you hadn’t thought of couldn’t there”? I mean in the case of nuclear war, for example, nuclear winter hadn’t been thought of until 1982 and 83 and so that’s a case where we had nuclear weapons from 1945 and there was a lot of conversation about how they could cause the end of the world perhaps, but they hadn’t stumbled upon a mechanism that actually really was one that really could pose a threat. But I don’t think it was misguided to think that perhaps it could cause the end of humanity at those early times, even when they hadn’t stumbled across the correct mechanism yet.

Arden Koehler: Because it was just an unprecedented event?

Toby Ord: Yeah, and there hadn’t been that many people searching for such mechanisms and they ended up kind of getting there from thinking about other planets. Planetary exploration made people think about how very different atmospheres worked and to get some kind of data on what it’s like to have radically different atmospheres or dust storms throughout the whole of Martian atmosphere and things like that. And that made them think about this. But you could easily imagine them just never having noticed that mechanism actually since the Cold War ended shortly after that. And so I think that this is just the kind of thing that on priors, it’s such a big change, but I want to stress that my best guess number for the chance of existential risk due to climate change is about one in a thousand over the century. And that’s mainly coming from this kind of, “I don’t know the mechanism, but that our models aren’t sufficiently good”.

Robert Wiblin: Hey everyone, Rob here — we realised we use the word ‘prior’ dozens of times without explaining it. And it is indeed a bit of a jargony term.

Prior is short for ‘prior probability’, and it originates from Bayesian statistics.

For today’s discussion: you can basically think of it as the thing you believe before you see new evidence.

Let’s say you have a standard 6-sided dice, and we’re looking at the probability of rolling a 2 on any given roll. We roll the dice, I see it, you don’t. I ask, what’s the probability that we rolled a 2? Your answer would be 1/6. That’s your prior.

Then I give you a hint: the number we rolled was even. Now what’s the probability that it’s a 2? 1/3. That’s called your ‘posterior probability’, updating on the evidence that the number was even.

A ‘uniform prior’ is when all possible values are equally likely before you see new evidence, or you have no prior information and you can’t distinguish between possible values. So in the case of the dice, there are six different options – so a uniform prior would say that each one has a 1/6 chance. That’s where you might start from before you consider any empirical evidence you’ve observed at all.

Slightly confusingly, In casual speech many people, including me probably in this episode, use ‘on priors’ to mean what we’d expect given our general background understanding of how the world works. So, for example, on priors I’d find it surprising for Taylor Swift to be elected president of the US, because that just doesn’t fit with my general understanding of how US politics functions.

There’s a more in depth discussion of priors and Bayesian inference in episode 39 – Spencer Greenberg on the scientific approach to solving difficult everyday questions.

And if you find the more in-depth discussion about priors later in the episode confusing, that’s very understandable, and you should feel totally fine skipping to the next chapter.

Alright, with that little diversion out of the way, let’s get back to the show.

Robert Wiblin: Yeah. I guess on the thing of the population shrinking… So imagine that the habitable surface of the Earth shrinks, let’s say 80% because we just got some massive warming. I guess putting my economics hat on, my concern is that maybe the population that could be sustained from the food in those areas then isn’t enough to maintain the level of specialization and industrial capacity that we have today. And so you get kind of stuck at some level of economic development where there aren’t enough researchers, there aren’t enough factories to produce say the microprocessors that would need to reach the next level of economic development. You could imagine, I feel like if the maximum number of people who could ever be alive at one point in time was a billion, that then we’d just get stuck technologically.

Toby Ord: It’s possible, although if you run the clock back and look at when there were a billion people, that would seem to set a kind of limit that you’d at least get to there. And then the idea that the bit where we happen to reach that point on our Earth, if you just stopped at that number and stayed there forever, we’d probably imagine there’d be at least quite a bit of extra growth you could have beyond that, particularly as you’ve got a lot of time and also we’ve even now developed a whole lot of these technologies and we would still know how they work and so on. even if we couldn’t devote as many scientists to them and so forth. It could be possible. Like some kind of scale argument like this I think eventually works. If there could only be 10 people–

Robert Wiblin: We’re not going to space.

Toby Ord: Yeah, I don’t think it’s just the case that you need to run things for 700 million times as long before we achieve our current level of economic development. I think that you just can’t get there. So I agree that this argument works at some point.

Arden Koehler: Yeah. I mean you might think the Earth at a billion people, although it would probably get to a much greater level of development than it was when it was at a billion people, if the potential of humanity, and we’re gonna get to this later, is as grand and open and could involve as many huge jumps in technology and ability as maybe it seems like it can right now, it does seem pretty plausible that you’d at least reduce that potential a decent amount by decreasing the chance that we’d ever be able to, for instance, get off the planet Earth.

Toby Ord: That’s interesting. And I’m not so sure that it would decrease it by much. But if it did, suppose it kind of decreased it by half, then it would be half as bad as if it was just an outright existential catastrophe. So that actually would change things a bit in the analysis. So therefore perhaps it is a useful thing to think about. You still have to get a very extreme event I should say before you can get to the kind of point where you’ve reduced the Earth’s habitable surface area by anything greater than a half.

Risk factors [01:10:53]
Robert Wiblin: Yeah. So you introduced this concept of risk factors, which is kind of what we’re talking about here to think about what about things that can’t kill us directly but then can kill us through some indirect mechanism. They might be significant. Do you want to talk about risk factors and how they apply to climate change and other things?

Toby Ord: Thanks. I think this is an idea that there’s some intuitive version of that’s been floating around for a long time, but I wanted to kind of make it a bit more precise so we know what we’re talking about. The idea as I think of it, is that there are certain things which are existential risks. So there’s some kind of threat, such as an asteroid or a supervolcano or climate change where that thing itself could lead to the destruction of humanity or humanity’s long-term potential. Those are the existential risks. But that’s just kind of one way of cutting up the total amount of risk. You could divide it into these silos or something or, you know, vertical slicing of it into different risks. But you could also cut it up in other ways. So you can ask a question such as, “What about if we got rid of the chance of great powers going to war with each other”? The kind of war like the First and Second World Wars and the Cold War perhaps as a cold example of such a war. What if we could eliminate that risk? Like how different would the total existential risk be over the coming century if we, say instead of having the world as it is, we could just press a button and make it so that there was definitely no great power war.

Toby Ord: My view on that is that it would remove something like a tenth of that risk over the next century because we would be able to deal with things in a situation of more cooperation on international levels which is quite important and less building of weapons. And if so, you know, on my one in six thing, then you get something like a one in 60 reduction, say something like a percentage point lowering of the total existential risk could be attributed to the current levels of threat of great power war. So on that idea, I think it’s actually quite an instructive way of thinking about it because I think there’s a tendency among effective altruists who are interested in existential risk to… Say suppose they hear that someone’s working on asteroid risk, they’d think, “Oh wow, you’re really actually doing it”.

Robert Wiblin: You’re nailing the real issue!

Toby Ord: Yeah, exactly. You’ve got this issue that I think is so important, centrally important to humanity’s future and just so important compared to everything else. Whereas if they hear that someone’s working on world peace or various forms of international relations to try to diffuse tensions between China and America, they might think, “Oh, that’s not one of my people” or something. But actually the asteroid risk is very low. It’s far lower than 1% over a century and it seems that we should take seriously these existential risk factors as other things that we could be working on. And one of the nice things about this formulation is that there’s an apples to apples comparison between the amount of risk posed by a risk factor or by a risk. And so you could actually compare them like that. It’s not an illegitimate thing to do. And then this means that you could perhaps focus on various forms of indirect risk which are created by things, even if those things themselves are not existential risks such as great power war. It’s a different category. For any kind of thing that you can imagine, you could just ask, “What if you didn’t have it”? And then you can understand this question of the risk factors, and they don’t have to add to one, which is another kind of issue about them.

Robert Wiblin: Because they overlap?

Toby Ord: Yeah, they effectively overlap, and so if you eliminate one, then you eliminate another one. It won’t do what it says on the tin for the second one. The first question was how much would it lower it compared to if you hadn’t pushed any of these other magical buttons that eliminate other risks or risk factors. So the maths does all work out, but they don’t have to add to one. And before I get to that on climate, I want to stress that this is a dangerous observation, to be thinking about it like this. I think that many things that we traditionally think of as important for society, such as even better education and things, that could be the opposite of a risk factor. A security factor so that if we ramped it up, that we would actually lower risk through that. But there’s this risk from all of that, that a whole lot of people who really cared about this issue just go and do generic work on things that everyone regards as important anyway, and that they work on things that are much less neglected and don’t work on things that are actually much higher leverage because they’re about particular risks which are themselves neglected.

Robert Wiblin: Or I guess things that are risk factors, but are small risk factors and so they shouldn’t be getting most of the attention.

Toby Ord: Yeah, either that it’s a small risk factor or that it’s a very big one, but almost everything actually bears upon it and so you’ll be making a very small contribution or that you can’t find ways to work on it that are as targeted as you can.

Arden Koehler: Is the concern that because once you introduce this way of reasoning where it’s like, “Look, it doesn’t have to be an existential risk for working on it to contribute to reducing existential risk”, it’s sort of seductive to maybe have some motivated reasoning that the thing you were hoping to work on anyway, because you really liked working on it in fact, it’s going to be one of those things?

Toby Ord: That’s the kind of idea. You can imagine, actually, if this goes wrong, just having access to this concept. Whereas I’m worried that without it we’re too insular and too focused on particular silo-based approach to risks and so on. But with it, we grow much larger but it gets too diffuse and the particular kind of specific things that we’re mentioning was where a lot of the value was in really prioritizing and that we lose that. So I do think one needs to be very careful with the idea.

Robert Wiblin: Yeah. Do you want to apply this to climate change now?

Toby Ord: Yeah. So I think that it’s often suggested that climate change might not be so much an existential risk, but that it’s something that would increase other existential risks. So in this case, my terminology would be a risk factor. I think that this is probably right. I think that if we imagine a world, if we could just somehow have the next century but make it so that climate change wasn’t an issue. All of the dedicated altruists who are working on fighting climate change could then work on other things and global international tensions on this would go down and so nations could spend their “altruistic international corporation” kind of budget on something else. So I do think that that could actually be quite helpful. As to how big it is as a risk factor, my guess would be somewhere between… these are very rough kind of guesses, between about 0.1% and 1%. So maybe a bit bigger as a risk factor, but not an order of magnitude. Probably not a whole order of magnitude bigger.

Robert Wiblin: So you think it’s quite a bit less important than war, or a great power war?

Toby Ord: My guess is that it is less important from the perspective of existential risk reduction.

Arden Koehler: Sounded like some of the main mechanisms you were thinking about by which this could be a risk factor is basically that it distracts people. So the budgets of these governments and of organizations and people’s personal careers will be spent on it instead of on other things that you think might be more important ultimately.

Toby Ord: Yeah. I think distracts is kind of right, but it has the wrong emphasis or something because you can think distraction can’t be that bad. Maybe a better way to think about it is this is a stressor on national and international relations and so forth.

Robert Wiblin: And our capacity to solve problems. So our capacity gets used up trying to solve this thing and then we don’t have headspace to think about something else.

Toby Ord: Yeah, that’s right.

Arden Koehler: What about if some moderately high level of warming comes about such that maybe this actually just ultimately falls into the bucket of reducing our capacity to solve problems, but it seems like if health systems and economic systems suffer a lot, it could leave us more vulnerable to things like pandemics, naturally occurring and engineered? Does that seem plausible?

Toby Ord: Yeah, I think it’s quite plausible that it could leave us more vulnerable to pandemics. Also the fact that effectively a larger part of the Earth would be in a tropical environment. So I think that this is something that is certainly recognized that there could be more endemic disease and maybe more pandemics as well. But one thing here is that some people are particularly concerned with something that’s called “double catastrophes”, you know, “Well, maybe that not on its own, but what if you had that and something else”? It’s worth noting what has to happen there. If they got these two small probabilities, say one in 100 and one in a 100, and you think, “Well, each one on its own”, but having them both together ends up being a one in 10,000 event, anyway. It’s what we call second order. And so it’s kind of a bit hard to get these arguments off the ground.

Toby Ord: Like the best version of this argument would say something like, “Well it’s a one in a hundred event, but there’s a one in 10 version of it which would be big enough to interact with other ones and another one in 10 version and together though, that just ends up at one in a hundred again, so it’s hard to actually get these things where they both have to happen to actually be likely enough”. You would kind of need some correlations between them to be really happening, but I’m not sure that this pandemics case induces enough of a correlation. Effectively, if the previous risk level was what I was saying for natural pandemic of about one in 10,000 per century–

Arden Koehler: Well that’s of us going extinct from an actual pandemic, not of a–

Toby Ord: Yeah, but then how much would a world with extreme climate change have to increase that chance by. You don’t have to really multiply it by a lot in order to be making a big difference there.

Robert Wiblin: For that to be the main way that’s having impact.

Toby Ord: Yeah, where you say, “Well, there’s a one in 20 chance that climate change is extreme beyond this level and then if you had that thing happening it would increase this other thing by a factor of 10”, but I think it’s hard to get these numbers to actually work out to be making large contributions. But I could be wrong about that. Maybe I’ve had trouble doing it, but other people haven’t really had that much of a go at it and I haven’t really been challenged on it. So I would be open to people putting together the scariest looking cases of how you could get these things interacting.

Arden Koehler: I mean one thing that what you’re saying suggests is that maybe some of the most serious ways in which climate change or something else could be a risk factor is by impacting the other bigger risks. So you know, even if you think there’s a plausible mechanism for increasing some other existential risk that we can think of, it really matters how big that other existential risk is for how much that translates into being a risk factor.

Toby Ord: Yeah, and so I think it may even be the case that, say the median level of climate change, like the stress that that creates on international institutions and governments and so forth, that that’s large enough to change the risk of, say, the biggest risks such as AI or engineered pandemics, to increase them by a 10th or something like that compared to if we definitely could just not have to worry about all of these challenges of climate change. That could be a mechanism that produces a significant amount of risk as a risk factor. But it’d be interesting to see some robust conversation about that rather than… This is just me kind of sketching out some combinations of numbers, where I find it a bit hard to see how it would really work. But the people at CSER, The Centre for the Study of Existential Risk in Cambridge in the UK, they are quite concerned about this and they think that climate change is a much bigger existential risk than I do. And they think this is largely through risk factors. Largely also through things to do with the collapse of civilization. So, you should talk to those guys.

Robert Wiblin: Yeah, we will. Yeah, we’ve got some episodes on climate change coming up. My anecdotal impression is that people are really drawn to these stories where multiple different things go wrong. And I wonder whether it’s related to this phenomenon where when you add more details to a story, even though it’s making it more specific and in a sense more unlikely because it’s more vivid and people can picture it better, they think it’s more likely, even though kind of strictly has to be less likely, the more things you add onto it.

Toby Ord: That could well be right. I don’t know. I mean, it has the problem though when you know a bit about the heuristics and biases–

Robert Wiblin: You can come up with a something for everything!

Toby Ord: Exactly. If you’re in an argument you can kind of think, “Maybe you’re just biased, because I’ve read a paper which didn’t replicate which suggests that you are–”

Robert Wiblin: You could come up with a very specific word like people have the ‘multiple risk bias’ that I just named and put capital letters on it and now it’s a thing.

Toby Ord: So it could be but it’s also somewhat dangerous.

Robert Wiblin: Yeah. A listener wrote in and was curious to know what you think of the argument that climate change is very in vogue this year, probably next year. It’s a very hot button political issue. So maybe that’s a reason to get on board and push it over the line in terms of getting major policies done. And so the fact that it’s not neglected right now in terms of its attention level is actually an argument in favor of working on it rather than the reverse.

Toby Ord: Hmm. I mean that’s an interesting argument. It could be that our opportunities are getting better. So, when I think about these things, I typically start with the importance, tractability and neglectedness model to work out how important a cause area is. In the case of existential risk, the importance is like the amount of risk, the percentage points of contribution of risk. And in the case of climate change, at least the typical case of climate change, we’re a lot less neglected. There’s a lot of emphasis on it, but as well as this neglectedness, importance and tractability, there’s also the question about your opportunity. I think that a lot of opportunities can be a hundred times better than others. And so that’s something where you can get a very big multiplier. And I think that’s what’s coming in here.

Robert Wiblin: Where suddenly the choice set of campaigns that you could consider running has expanded a great deal.

Toby Ord: So I normally think of the importance, tractability and neglectedness at the cause area level, and then the opportunity at hand and perhaps your skill set as at the individual level when you’re thinking about these things. Then ultimately you get this product of all of these factors as an estimate of the cost effectiveness. A very rough estimate of working on something. But this does seem to be a case where maybe some of this leverage type thing or the opportunity is actually coming at the cause level for the whole cause rather than just for a particular intervention.

Arden Koehler: Wouldn’t we want to just say that’s a way in which climate change is getting more tractable?

Toby Ord: Yeah. You could put it that way. You also run into issues about, well, if it is so tractable at the moment, then won’t that kind of work out on its own? Like if we’re thinking about how much of the risk is remaining, certainly if you say, “It’s really tractable everyone, come and have a look at this”, then the argument seems to run into a bit of trouble because if it’s really tractable and there are millions of people who passionately care about it and devoting their lives to it, you have to kind of argue that it’s quite tractable but not quite tractable enough, so there are some complications to getting this story to work.

Arden Koehler: Or that it’s more tractable than people realize.

Toby Ord: Yeah. I still don’t know though. With climate change, it seems that there’s also a pretty reasonable viewpoint, which is that it’s very intractable and that sure, there’s a lot of people marching on the streets about it at the moment, but even despite all the people marching on the streets, you can still see that governments are really dragging their heels on it. And so actually that’s evidence that it’s really hard to do anything about it. And particularly it’s very hard to be the million and one person on the streets to really be making a difference once there’s those other million people doing it. So I’m not really sure how it shakes down overall, but I’m open to the idea.

Arden Koehler: I guess the best case for it being a hot button political issue being a reason to work on it, is if we thought there were tipping points or if you could just do this small thing then that would really set in motion a lot of momentum.

Toby Ord: When it comes to climate change. I’m very glad that a whole lot of people are working on it. But I think when I think about effective altruism, or people listening to this podcast, I think that what we should be doing is thinking about the kind of portfolio of attention that the world has on a whole lot of different important issues and what kind of marginal change to that portfolio would you like to see? And I think that what I would like to see in the overall level is extra attention to the idea of existential risk on the whole as opposed to particular cause area things or to the areas that have higher risk than with climate change or that are more neglected. But for climate change, in particular, my advice would be more pointed. So, for example, that there should be substantially more research on extreme warming.

Arden Koehler: Right, more than that one Nature paper you mentioned.

Toby Ord: Yeah. Well, I mean, there’s more research than that. But that’s the thing that often gets cited is if it’s kind of case closed, there’s a Nature paper, which is not how science works. But I think that better characterization of the chance of extreme warming and better understanding about how bad it would be and could we survive the extreme warming and could there really be cases or blue sky thinking about… We understand a bit about various mechanisms which would cause the kind of central case of damage that we’re thinking about when economists model a damage function of warming and they’re thinking about extra disease burden, extra kind of adaptation, crop failure and so on. But rather to think, “Are there any things that, you know, like in the case of nuclear winter, some really quite different mechanism which could cause a different kind of threat that only happens when it gets to a very high level”? Blue sky thinking about that could be extremely valuable and could then help us much better understand how much of a risk climate change poses.

Biological threats [01:26:59]
Robert Wiblin: All right, let’s push on. There’s unfortunately tons of threats to get through. So the next one in the book is biological threats. So we’ve got both natural pandemics and ways that biotechnology could make things worse, which is super topical the week that we’re recording because this new coronavirus is all over the news. Yeah, help set the scene. How bad have pandemics gotten through history? There were some absolutely eye-popping numbers. I guess I kind of knew this on some level, but then to see it all written out, just one after another, then you’re like, “Wow! Pandemics are bad”.

Toby Ord: So yes, three of the biggest cases of fatalities from pandemics in history where the Black Death, which killed somewhere between about a quarter and half of all people in Europe when it happened, which was somewhere between about five and 14% of the world’s population. So very roughly something like a 10th of the people in the world. The Colombian exchange, when the Europeans visited the Americas and exchanged their diseases, killed a very large number of people in the Americas. It’s hard to work out exactly how many, partly because there’s a lot of war and colonial occupation involved as well. And also we don’t know what the preexisting population size was, but it could have killed up to 90% of the people in the Americas and up to again about 10% of people in the whole world. And then the Spanish flu killed, again, that was about 5% of the people in the world. So there are a few examples that are actually quite different in how they worked, but that could get up to that kind of level.

Arden Koehler: So it seems like you think that natural pandemics, like the ones you’ve listed, although extremely serious, pose a pretty tiny chance, one in 10,000, of causing extinction in the next century. Whereas you think engineered pandemics pose a dramatically higher risk, one in 30. Why the huge difference?

Toby Ord: Yes. So the main reasons are that there is this natural risk argument that we discussed earlier whereby the total amount of natural risk can’t really be much higher than about one in 10,000 per century. And so part of that comes down to how much that argument applies to these natural pandemics. I suggested earlier that it doesn’t quite apply because they may have gotten less safe in some ways, but there’s also many ways in which we’ve gotten more safe. We understand diseases much better with the germ theory of disease. We have antibiotics, we have quarantine ideas and so on, and we’re spread much further across the world and so forth. So we have a whole lot of reasons why we’re actually more safe or less safe. And it’s hard to be sure how that all balances out. I think it leaves things somewhere in the ballpark that the natural risks is in the same level. Whereas when it comes to the engineered pandemics that we could have, there are several different ways that could happen when I’m talking about engineered pandemics to start with. There are cases of gain-of-function research where scientists make diseases more deadly or more infectious in the lab. So that’s a case where they’re being engineered for these bad qualities.

Toby Ord: The idea is obviously to help us overall by better understanding what genetic mutations need to happen in order for this to become more lethal or more infectious so that then we can do better disease surveillance in the wild and check for these mutations. Things like that. But they pose their own risks. But I don’t think much of the risk comes from that though, partly because even if it did escape, it’s still again very difficult for it to kill everyone in the world because it’s not that different from the wild types of these diseases. It’s somewhat worse, but they’re not making it thousands of times worse or something. And then there’s also cases of diseases that are engineered for use in war: so biowarfare. And that is quite alarming because they’re trying to make them much worse. And we have a lot of known cases of that. And then there’s also possibilities of what we often think of as terrorist groups, but perhaps cults that are omnicidal and have some plan to kill everyone in the world or something like this. And they actually are at least attempting to make the thing to exactly design the thing that could kill everyone, but they’re much less resourced than a military is. So there’s a few different kinds of ways they could be engineered. But the thing that they have in common is that they’re kind of working towards an actual objective of widespread destruction, potentially aiming to kill everyone in a way that the natural things are not. They’re trying to maximize inclusive genetic fitness is what they’re being optimized for, which is not the same as killing your host. They only kill the host inasmuch as that helps them spread. So it’s quite different to what’s happening there and that’s the agency or the fact that someone’s actually trying to make something that would wipe out humanity is what makes the chance so much higher.

Arden Koehler: Or at least trying to make something that will wipe out a lot of people. I mean, in the case of the bioweapons, presumably they would be trying quite hard not to make the bioweapon end up infecting their own people as well. But at least there, it’s not just a side effect that this disease kills people.

Toby Ord: That’s right. You can see that those three examples kind of ramping up the amount of agency trying to optimize for this terrible outcome as you go through, but also decreasing the amount of power or something like that where at the moment, some omnicidal group is perhaps the least likely because they’re the least powerful. But with this massive democratization of technology in biological sciences where what was only able to be done by a Nobel prize winning scientist or where they get a Nobel prize for that work, then a few years later it can be done by students. This is the trend when you look at things like CRISPR and gene drives. I think it’s a one year delay in those cases before students can do it. So these are cases where this democratization is at some level fantastic. People are very excited about it. But this has this dark side, which is that the pool of people that could include someone who has these omnicidal tendencies grows many, many times larger, thousands or millions of times larger as this technology is democratized, and you have more chance that you get one of these people with this very rare set of motivations where they’re so misanthropic as to try to cause this worldwide catastrophe.

Arden Koehler: So do you think more of that one in 30 comes from people or small groups with omnicidal tendencies, than from nations engaging in biowarfare that goes wrong?

Toby Ord: My guess would be over the century that more of it does come from that category.

Robert Wiblin: Yeah, speaking of weapons from states, to what extent do you think the Biological Weapons Convention helps with this, or to what extent doesn’t it help?

Toby Ord: Yeah, I mean it’s great that we’ve got a Biological Weapons Convention, but it’s grossly underfunded and understaffed. It’s sometimes talked about as if of course we’re fine because just like with the Chemical Weapons Convention and nuclear nonproliferation agreements, that we’ve got this Biological Weapons Convention that nations are signed on to, but many nations continued making bioweapons programs in breach of this. The Soviets were known to do so for many years after they signed on and the entire BWC, the total funding for it is about as much as an average McDonald’s restaurant. So it’s not going to single-handedly save us from this.

Arden Koehler: That’s just very absurd-sounding on its face, I guess.

Robert Wiblin: I have heard that before. The thing that I find odd about that is just wouldn’t some random donor, like some billionaire just throw them some money and then they can hire a fourth staff member or something? Like how is this a sustainable level?

Toby Ord: Yeah, it’s a bit tricky because I think the official permanent staff count was listed in the initial signing of the treaty. So it needs to get changed.

Robert Wiblin: To have four…

Arden Koehler: What a strange thing to do.

Robert Wiblin: Amazing.

Toby Ord: I think probably so that they guaranteed they had at least three, but it ended up carrying on or something. I’m not an expert on that, but something in that area, I think, and it may be that they can’t just accept funding from a private individual or if a particular nation decided to say, “We’re just going to ramp up the funding by a factor of 10”, that might look like they’re trying to get their way with the BWC or something like that. So I think that being a certain kind of international body, it might need to get broad support and it might be hard to unilaterally fix that problem. But if people pointed out the problem and showed their willingness and openness to fund up to whatever levels are required and then started to build a club of countries that agreed that that was a serious issue, then you could probably get it to work.

Robert Wiblin: I find it a bit odd that we haven’t managed to empower the BWC a bit more because as far as we know, the major powers are not working on biological weapons programs. It’s not commonly believed that, you know, China is developing biological weapons, at least not in any significant amount or to any significant degree. So it seems like they’d be keen to make it more powerful.

Toby Ord: Yeah, I’m not sure. One of the sticking points that often comes up is to do with verification powers. And it is more difficult than in the case of nuclear to be sure that someone isn’t working on it. And so this is one of the challenges of getting it to work. And so there are actually technical challenges here. It’s not just the case that people are wildly neglecting it, but I think that they should be taking it more seriously all the same.

Robert Wiblin: Yeah. You mentioned in this chapter that obviously it would be a bit stupid of you to go and write a recipe of what would be the most dangerous thing, or create a list of the ways that things could go worse. That would be a bit counterproductive, potentially. To what extent did you feel you had to kind of bite your tongue in this section on what you think might be the worst?

Toby Ord: Quite a lot.

Robert Wiblin: Okay.

Toby Ord: It is unfortunately one of these things that sometimes comes up in effective altruism where people say, “Well, people talk about bio as a big risk, but it’s really not going to be able to kill everyone. Here’s why. How would you get around any of these things”? And you know, you really hope that no one responds to that person with answers to that. But, by the same token, you can’t just trust people who say, “No, I’ve seen crazy things. Listen to me”. But it’s really unfortunate. It’s just part of the state of the debate in areas where there are serious information hazards. But it’s not the case that you should just trust the people who say that they’ve heard scary things. I think it’s a real challenge to epistemically work out as a community how to get through such things.

Nuclear war [01:36:34]
Robert Wiblin: All right, let’s move on and talk about nuclear war. How do you go about trying to estimate the risks that we face of nuclear war?

Toby Ord: That is indeed quite difficult. I give existential risk over the next century from nuclear war at about one in a thousand. I initially thought it would be higher than that. That’s actually something that while researching the book, thought was a lower risk than I had initially thought. And how I’d break it down is to something like a 5% chance of a full-scale nuclear war in the next century and a 2% chance that that would be the end of human potential.

Arden Koehler: Okay. So the 5% comes primarily from geopolitical considerations about who is actually likely to go to war. And then the 2% is thinking about how likely we are to actually go extinct if people go to war. And that’s going to be considerations about nuclear winter maybe or about the possibility of us all actually just dying in a nuclear attack.

Toby Ord: Yeah, that’s right. So nuclear winter is the main known mechanism. But when looking into this, it does seem that it does look fairly plausible and also very severe. But it is difficult for it to cause an extinction event for humanity. And one of the things that actually was the most compelling to me was not so much a particular piece of science about that, but the fact that all the people currently working on nuclear winter don’t suggest that it could cause human extinction and actively if asked about it say they don’t really see how that could happen. Carl Sagan, who is no longer with us, he did think that it could cause human extinction. So it’s not the case that everyone who’s ever thought about it, has thought it couldn’t cause this. But, the current community who you might think would be the type of people who’d be most likely to have extreme views that it would be really bad because they’re the ones who are working on it, they actually don’t suggest that it would cause human extinction. And if you look at a place like New Zealand or the Southeast of Australia, they are coastal areas. And also could do a lot of fishing. And it’s unclear why there would actually be any kind of collapse of civilizations, say in New Zealand. They might not be able to get new microprocessors from China, but in terms of continuing on industrial society and so forth in a world with nuclear winter, while it would be very bad elsewhere, it’s just very hard to actually make the story about why it’s bad everywhere.

Arden Koehler: And I guess it wouldn’t plausibly be combined in a scenario where New Zealand actually gets destroyed directly by nuclear weapons and we have nuclear winter.

Toby Ord: Not usually.

Arden Koehler: Because it’s just not a big target.

Toby Ord: That’s right. Something that New Zealand is probably pretty happy about. There was a moment when I was growing up and a whole lot of online satellite photography came out, including satellites of Melbourne, which is very useful. It was declassified Russian intelligence. But Sydney weren’t able to see the satellite photos of their own city because it was still a target of the Russian nuclear system. But they’d decided that Melbourne was not a target. So we were at least a little bit relieved about that, although a little bit surprised in retrospect that we were ever a target.

Robert Wiblin: I guess they have Google maps now, right?

Toby Ord: Yeah, we don’t need to rely on this now, but it was just a moment from my childhood where this kind of came up. Ultimately, when we had the period of the Cold War, there were many different mechanisms posed, including fallout which was the main one. But then we realized that actually the fallout from all of the nuclear weapons that we had at the height of the Cold War arsenal wouldn’t really be able to impose an extinction risk. But, how do we know that there won’t be much larger weapons built or many more weapons built in a future arms race? A lot of things that we would have thought of as crazy; why did they build so many weapons? What would stop them building 10 times as many again or a hundred times as many again in a future build up. Maybe the game theory of it would actually lead in that direction to do with certain kinds of instability of protecting your weapons or something. If your weapons are really vulnerable, maybe you need a hundred times as many because you’re going to lose 99% of them in a first strike or something like that. There could be some kind of situation where all of a sudden, the fallout risk actually gets on the cards and then all of this concern about nuclear winter is somewhat moot.

Toby Ord: So over a long period we’re a bit unsure. And then there’s also this issue that with climate change, it’s just such a big change to the world’s climate and such a major unprecedented thing in human history to cause this amount of soot in the upper atmosphere, and this darkening and cooling of the world, that I’m just worried about unmodeled things and that again, the fact that we went for 38 years of nuclear weapons era before people even suggested nuclear winter means that there could well be things like that that we just haven’t discovered yet and that we’re not focusing on and we’re solving the wrong problem or something when we’re looking at this. So it’s mainly that kind of residual types of risk which concern me.

Robert Wiblin: Yeah, so we somewhat covered this in the climate change section, but kind of imagining a world where there’s a massive nuclear war and most of the surviving people are in New Zealand or Chile or Argentina or whatever. I guess it seems like most people think that it’s very likely that those people would then be able rebuild all of the civilization that we have now, and then potentially eventually more later on. That basically there’s a very good chance it would recover. Are there any reasons for thinking that we just might not recover? I know sometimes people mention, for example, that we would have used up all the fossil fuels, so that it’d be harder for them to build up again.

Toby Ord: So I think that this is a very uncertain issue. So when I talk about existential risk, I’m using a definition that’s based on that of Nick Bostrom and slightly evolved. Where the idea is that we’re interested in extinction risk, but we’re also interested in another kind of bundle of things that are importantly similar to extinction where, for example, the fact that we can’t even afford to have even one of these catastrophes is true for all of them. They have a lot of methodology in common and a lot of similar aspects to do with how they destroy our potential. They’re all things that destroy not just the present, but make us lose our entire future. And one of these would be extinction, but another would be some kind of unrecoverable collapse of civilization. So I want to take that seriously, but I don’t really make claims in the book as to whether it’s likely or not likely. I think that it depends a little bit on the risk as to whether the contribution via an unrecoverable collapse of civilization is higher or lower than the contribution via a direct extinction. And I think you’ll find that people have very different views on this probability of recovery. Some people think that it’s 99.9% chance we’ll recover. And really some people think that it’s like a 90% chance we won’t recover. And it’s very wide disagreement about a topic that we have very little actual information on. So I’ve tried to be fairly cautious about that since I’m not an expert on it to treat it as a live possibility, but something that I’m not putting all my weight on.

Arden Koehler: Shouldn’t the natural extinction rate come in again as a possible source of evidence here? So if civilizational collapse… I mean we haven’t really said what that means, but I’m assuming it means something like we’re not producing a lot of technology. We’re not using a lot of technology. In some sense, things have gone back in time. Then shouldn’t we see the one in 2000 chance per century as a decent guide?

Toby Ord: The problem here is that we’ve only had about a hundred centuries of civilization. And so actually it’s like a hundred centuries since we had agriculture, but about 50 centuries since we had cities and writing and law and things like that. And the equivalent number ends up being 2% risk in this century, which is not really low enough to make some of these arguments. And also, we think that it’s often our industrial technologies, which are the types of things that could be causing this. And we’ve only had a couple of centuries since the industrial revolution where the number that comes out of the analysis is 50% per century risk. So you can’t really use these arguments to bound this too much. You can use some other things though. So when people talk about civilization collapse: it’s a fascinating area, I think, for people in existential risk. A lot of the literature on it is just about individual civilizations, such as a particular dynasty of Egyptian civilization collapsing where they treat, say, Egypt as several civilizations as opposed to treating say Western Europe as a civilization or something like that. It’s very fine-grained, typically. But what we’re talking about is, at the very least, a global collapse of civilization. And then sometimes that is thought about as things moving to a pre-industrial time. But I’m talking about it in the book that the level that I think is most salient, that I’m using, is that there is no civilization. So it’s in the same way that 15,000 years ago, there was no civilization and what would be needed to get such a severe level of collapse. It could be that I’m analyzing it at the wrong level and that the dangers are more from having smaller levels of collapse is sufficiently more likely. That even though we’re more likely to recover, there’s still a greater chance of screwing things up. It’s very unclear, but for my purposes, I’m thinking of it as there’s no civilization anymore and it’s very hard to see how nuclear war could get you to that level. Also there’s a kind of reassuring aspect that civilization has independently developed more than five times in different parts of the world from pre-civilized world. So that’s something where therefore it’s very hard to think that there’s only a ten percent chance that civilization would come back or something since why did it come so many times so far?

Robert Wiblin: Interestingly, we’ve only had one industrial revolution, though. So what if we go back to 1500? And I guess some people think that the industrial revolution was very contingent on particular aspects of technology and politics. Not everyone, but yeah.

Toby Ord: Yeah. So that’s a different approach. I think at Open Phil, their writings on this have been more concerned about that level. So what would be needed to knock things back to a pre-industrial world and then the chance of getting industry back. I think that’s interesting and there should be more discussion of what’s the relevant level that does most of the work and that one, people who think that the values that came out of this change as well… Something that’s very fragile and if you got industrial civilization back they’d have different values. That’s another potential argument, not one that I draw upon, but that some people make.

Arden Koehler: So what’s wrong with the following argument, which is what I was trying to get at before, which I might just be confused about; if civilization completely collapses such that there is no civilization, shouldn’t we see the existential risk levels dramatically drop because it’ll be almost as if there were never a civilization and then we should go back to that natural extinction rate?

Toby Ord: I think that’s roughly right. It does depend on how you got there. So if we got there through massive global warming, then we’d be in a world that might be importantly different and that’s certainly something that the people who are worried about that would stress. But, it could be that the risk levels go down. Again, the way I think about this is that it’s not that the collapsed civilization would then go on forever, to the end of time, as an alternative to extinction. It’s rather that it would be more likely to end it state of non-civilized world by moving to extinction than by moving upwards to a civilized world or some kind of fulfilling of humanity’s potential such that the event that knocked out civilization would be the key event in human history. That’s the property that I think is needed in order to make that the existential catastrophe.

Arden Koehler: I see. So this is why it depends so much on how likely it is that civilization comes up again. Because if it were super unlikely, then if there were just no civilization again, maybe we would just continue on for an extremely long time until we die out naturally. But if it’s much more likely, then it’s going to be a lot less dangerous from an x-risk perspective.

Toby Ord: Yeah.

Robert Wiblin: You have this really nice point in the book about how people talked about civilizational collapse in the past. So the Roman empire collapsed in some sense: it became like more politically fragmented and disorganized. But that doesn’t mean that many of the people there died or that the city ceased to exist. And even the Eastern part of it kind of continued on at a pace and it didn’t affect China or the Americas. It actually got quite a localized political breakdown.

Toby Ord: That’s right. And so from my view, I failed to see why almost any of these numbers on civilizational lifetimes and things like that are relevant at all. I think that there is some case someone could make that they’re relevant. For example, they could say that, “We’re so interconnected now that the level of interconnectedness of the world is similar to the interconnectedness of one of these previous civilizations”. I don’t think it’s quite true, but if they could make that case, then maybe that would kind of suggest why it’s the relevant unit of inquiry. But a useful example I think is this case with the Black Death that killed something like a third of the people in Europe and it didn’t cause any kind of regional collapse of civilization. Things just kind of moved through. And so it seems like this is the kind of case where we do seem to be quite robust.

Robert Wiblin: It might say something about the rate of political collapse of big countries or something like that, but then this is quite a different issue, right?

Toby Ord: Yeah. A country’s very different. And also the word ‘civilization’ has partly just been used with two different meanings here. There’s this meaning of like a planetary civilization and there’s a meaning of, say the Egyptians, as opposed to the Assyrians or something.

Artificial intelligence [01:48:55]
Robert Wiblin: All right, let’s push on. So you actually placed the biggest risk, as we said at the start, on risk from unaligned artificial intelligence. I think you say it’s about a one in 10 chance that this could do us in within the next century. It’s a little bit odd that we’re not going to spend more time talking about this in this interview, but I guess we’ve had so many interviews about AI in the past and we’ve got several already recorded, so we risk flogging a dead horse a little bit. But yeah. Why do you think that the risk from unaligned AI is so high?

Toby Ord: Yeah, I say quite a bit in detail about how I see the situation, in the book. But I think that a useful bird’s eye view of it all is actually helpful. I think that you can divide into these two parts. One of them is, “What’s the chance that we will develop something more intelligent than humanity in the next 100 years”? And then, if we did, as I point out, humanity has got to this privileged position, where it’s humans who are in control of our destiny, and control of the future of the Earth-based life, in a way that, say, blackbirds or orangutans aren’t because we have unique cognitive abilities. That’s both what we think of as our intelligence and also our ability to communicate, and to learn and so forth, and to work together as teams, both within a generation, and between generations.

Toby Ord: It’s something broadly like our intelligence that put us in this unique position. We’re talking about creating something that knocks us out of that position. So, we lose what was unique about us in controlling our potential and our future. Then, one question is what’s the chance that we develop something like that? Then, the other question is, “If we develop it conditional upon that, what’s the chance that we lose our whole potential”? Basically, you can look at my 10% as, there’s about a 50% chance that we create something that’s more intelligent than humanity this century. And then there’s only an 80% chance that we manage to survive that transition, being in charge of our future. If you put that together, you get a 10% chance that’s the time where we lost control of the future in a negative way.

Toby Ord: With that number, I’ve spent a lot of time thinking about this. Actually, my first degree was in computer science, and I’ve been involved in artificial intelligence for a long time, although it’s not what I did my PhD on. But, if you ask the typical AI expert’s view of the chance that we develop smarter than human AGI, artificial general intelligence, this century is about 50%. If you survey the public, which has been done, it’s about 50%. So, my 50% is both based on the information I know actually about what’s going on in AI, and also is in line with all of the relevant outside views. It feels difficult to have a wildly different number on that. The onus would be on the other person.

Toby Ord: Then, the question is why would they think that we have much higher than an 80% chance of surviving this ‘passing this baton to these other entities’, but still retaining control of our future or making sure that they build a future that is excellent, surpassingly good by our own perspective? I think that the very people who are working on trying to actually make sure that artificial intelligence would be aligned with our values are finding it extremely difficult. They’re not that hopeful about it. So it seems hard to think there’s more than 80% chance, based on what we know, to get through that.

Robert Wiblin: Yeah. I guess, for someone to say, “I’m 95% confident that if we invent artificial general intelligence, that it will go well, and we’ll be able to control it”. I guess there’s a sense in which that’s a quite strong claim, because it’s like saying, “This thing that doesn’t exist yet, that I’m not sure how it will work, and that seems like it would be very influential, I’m fairly confident it will be safe.” It’s really a bit of an odd combination.

Toby Ord: Yeah. It’d be, I think, a strong claim. I think a lot of people who make it wouldn’t quite realize how strong it is. But, it’s not an unreasonable claim. I think that my order of magnitude here is roughly right, but if someone said, “Well, actually I disagree with you, Toby. I think that the chance of risk from AI this century is 2%.” I mean, my number is just not all that different, really, from 2%. It doesn’t require that much evidence to shift you by a factor of five in this area that’s very uncertain and relies on a lot of judgment. Also, the actions that you should take are not that different if it’s 2% to if it’s 10%. It’s not clear that there’s that much at stake in that case.

Arden Koehler: I think what makes it feel like a stronger claim, which is the test that we use for estimating the risk from nukes, is this is a 20 or a 5% chance that we will either all die, or things will go completely off the rails, and even though everyone wouldn’t want this, and it’s from something that comes from our own actions. So, I feel like once those things are all there, that would make it feel like a stronger claim to say, “Well, there’s only an 80% chance that this won’t happen”.

Toby Ord: Yeah, I think that’s right. It’s a very interesting type of argument there, that the more obvious it is that AI would be a risk, the more compelling that is, in some ways, maybe the less risk there would be, because once you get a case where there’s 100% risk, or it’s super clear, then you’d hope that no one would actually turn this thing on or finish building it.

Toby Ord: I think that argument doesn’t work quite as well as you might hope. If you apply it to nuclear weapons, and to other areas, there are strategic incentives to build things that could be very bad. The fact that nuclear weapons could create assured mutual destruction just fed right into the incentives that people had. That was considered a plus in some of the analysis when these decision makers were deciding whether to renew their arsenals. You’ve got to be very careful about that. But also, what I’m more worried about is that the arguments will always be a bit uncertain, and that they will be the kind of arguments that maybe should push a rational person to think that there’s a 20% chance that this will all go wrong, but that some people would just be willing to take such a 20% chance. Or, that they will be selected for being the people… Not everyone will say it’s exactly 20%, some people will say it’s 50%, some people will say it’s 2%. It turns out the ones who think it’s small will be the ones who then unilaterally make these actions, when there are pressures to develop these technologies, economic pressures, or social, or military pressures.

Robert Wiblin: Yeah. One way that AI ends up really standing out in your analysis… You divide these three steps that you need in order for everyone to die or, I guess, everyone to lose control of the future. You’ve got to have something that arises, and then spreads out over the whole world so it can affect everyone. Then also, that it finishes the job. So, you have this problem with a disease, how does it reach the 1% of hardest to reach people in really remote places and nuclear submarines and all that? I guess with AI, even if it’s quite unlikely to arise, it’s a lot easier to see how these later steps happen, because it has this motivation to spread. It actually has intent in a way that a disease doesn’t.

Toby Ord: Yeah. Or it’s at least easier to see at some very high level because of the intent. It’s actually trying to wrest control of the future. A couple of things that I just want to explain, though. A lot of people don’t quite see how the scaling up would work because they’re thinking about robots, though it’s probably less so among your audience. But ultimately, without any kind of robotic manipulators, AI could… If you think about Stalin or Hitler, we have people who scaled up from being one person, to being in control of a significant fraction of the world’s military power. Most of the orders of magnitude, up to the whole power, they scaled. They did so through manipulation of other humans.

Toby Ord: You can imagine AI systems on the Internet spreading to millions of unsecured computers and trying to manipulate millions of people who are on the Internet into doing their physical bidding by paying them or threatening them or enticing them; promising them things in the future. I do think that–

Robert Wiblin: It seems like even humans who aren’t super sophisticated sometimes seem to pull this off. Yeah, influencing very large numbers of people to do strange things.

Toby Ord: Yeah. I paint a picture of this in the book of perhaps how this could happen. It’s not meant to be the only picture, but it’s meant to show how, by building up a whole lot of abilities that humans have already achieved. Things that are clearly within human level of intelligence. Basically, building a large scale criminal underworld. That AI going through that route could scale it’s way up to the power of a Nation State or something. Then, it’d be almost impossible to eradicate, as well. That’s a bit of an explanation of the scaling step.

Toby Ord: As to the final step, I’m not claiming that AI is an extinction risk. I think that it’s not clear that even an AI that went badly wrong would want to kill everyone. I think that humans are the most interesting thing that it would have access to, possibly the most interesting thing in the affectable part of the Universe. But that doesn’t make a substantial change. I don’t think they’ll be saying, “Okay, humans, fill the Universe with love and flourishing and all the things you want”. Our future would be radically curtailed if we were just there as something for them.

Robert Wiblin: At the behest of them.

Toby Ord: Yeah, at the behest of AI. And whatever goal function it was programmed with, it would be attempting to achieve that using us as an interesting piece of evidence to help it better achieve that goal, rather than listening to us and doing what we want. It would count as an existential catastrophe, though not necessarily claiming it would be an extinction catastrophe.

Arden Koehler: So zooming out a little bit, it feels like there’s a bit of a pattern with how likely you think various extinction risks, or existential risks are. Where the more unprecedented something is, basically, maybe the more uncertainties around it, and therefore the less this reassuring evidence that we have in other cases applies. I’m wondering if that’s just a pattern that happens to be there, or if you think that’s actually driving part of why AI, which is maybe the most unprecedented, you think is the biggest risk, and then engineered pandemics is pretty unprecedented, but we’ve seen pandemics?

Toby Ord: Yeah, that’s a good point. I do think there’s a strong connection here. It’s mainly coming from this fact that the more precedent you have, the more data you have to confirm that the rates are low. Another way to look at this is that the uncertainty generally counts against you in these cases, where people often say, “Well, you say that nuclear winter would kill this many people, but there’s a whole lot of uncertainty remaining”. That uncertainly is generally bad. If we knew it would only kill that many people, then we would know it’s not an extinction risk. It’s the uncertainty remaining that actually makes us worried that it could be. I think that’s often the case with these things.

Toby Ord: It does mean that these big numbers, for big uncertain risks, could change the most. They could change the most with the smallest amount of additional evidence because they’re uncertain. You can imagine that there’s some fundamental chance that a very informed person, more informed than anyone alive today, would have about what’s the chance of a catastrophe from AI, but I don’t know what that ultimate chance is. So, I’ve just got an estimate of it which is distributed over a broad range and I take an average of that, and that’s my overall estimate. Whereas, when we get more evidence, that range may well collapse down.

Dealing with big uncertainties [01:59:17
Arden Koehler: So this leads into the question of how we should be dealing with these big uncertainties? One approach would be, well, when you’re really uncertain about something, you should be conservative in your estimates and you should have this more conservative prior and then, if your evidence is not that strong, don’t update that far from that, and end up thinking, “Well, we haven’t all died yet, so probably we won’t in the future”. But, it seems like that’s not your approach?

Toby Ord: Yeah. It’s an interesting angle here. There does seem to be some kind of a distinction in how people treat this. My feeling is there’s a certain kind of traditional science approach. Like a falsificationist kind of science approach, where your answer is like, “You think this radical thing could happen that would be the most important thing ever, you know, prove it”. Like, I’m just going to sit here, and the onus is on you to prove this thing. I’m starting with this very tiny probability, and you’ve got to do the work to get it up higher.

Toby Ord: Whereas, what I’m thinking in this case of AI risk, is that it’s not quite agreement, but the typical AI researcher thinks there’s a 50% chance that we’ll develop something that dethrones humans in terms of the most intelligent thing in the known Universe: that that’ll happen, and taking them on their word, and then I think there’s some kind of reasonable chance that we won’t continue to call the shots in the future. Let’s say a chance, somewhere between 5% and 95%. I don’t see why one should assume, “There’s 100% chance we’ll continue to call the shots”. Or, equivalently, “There’s almost zero starting chance and then you’ve got to prove it to me”.

Toby Ord: What I’m kind of suggesting is, I’m just taking the traditional Bayesian approach to this, where you start off with some kind of priors or impressions about the thing, and then if there’s enough evidence, then maybe that would drive everyone to the same kind of probability that they assigned to it. But unfortunately, these are cases without that much evidence, so we don’t necessarily all get moved to the same end point. But, I think that the approach of skeptical prior, or something, it feels to me it’s more performing some role in the discourse of science or something like that. Maybe it’s doing some kind of instrumental work, but it’s just not how rationality behaves. What is a skeptical stance on something? You should take a realistic stance on everything. A skeptical stance on something is only relevant if it’s to solve some kind of social problem, such as a problem of false positives occurring, or people being biased in some way, or something like that. I think the approach I’m taking, while in some ways it’s unusual, it is, I think, just mainstream, Bayesian approach.

Robert Wiblin: Yeah. Every so often you hear people make this mistake where they say, “Oh, we don’t know what affect climate change is going to have. We’re just radically uncertain, so we should do anything about it”. Not so much these days. But, that’s just a mistake. In fact, the more uncertain you are about it, the worse, because that leaves open the possibility that it could be extremely bad and makes you worry more.

Robert Wiblin: I guess, with AI as well, sometimes you hear people say, “We have no idea what AI will look like, so why are we talking about this? Why would we do anything about this”? But actually, that’s deeply disturbing. You should be alarmed. Potentially, the thing that we might make that’s incredibly influential and we have no idea what it will be like?

Toby Ord: That should, indeed, make us very alarmed. The sensible version perhaps of that kind of argument is not so much that therefore the probability’s low, but maybe it could say it’s not super high. Like, you can’t say it’s 90% chance of risk from it if we don’t know what it’s going to look like. But also, they could be saying that now’s not the sweet time to work on it while we’re so uncertain about what it’s going to look like. I would agree with them on that aspect. That it may be that a given unit of work perhaps could have more impact if we wait until we find out what form AI’s going to take. If it takes a form, I should say, that is very much not like an agent, and, it’s in fact, no one’s really able to or willing to turn it into an agent, then I’m a lot less worried about it. It’s the ones where the analogy of, “What puts humans in this unique position,” where that analogy’s strongest are the cases I’m most concerned about. If it was the case that it’s very intelligent, but it’s just this oracular question-answering system, then the analogy doesn’t work that well because it’s not remotely like a species at that point. So that would be one of the hopeful outcomes, I think. If it was like that and there was no way to make it like an agent or no willingness to make it like an agent.

Arden Koehler: It wouldn’t want to wrest control of the future?

Toby Ord: Well, if it was just answering questions, then perhaps it wouldn’t want anything, yeah.

Robert Wiblin: What about it wants to answer the questions even better? The idea of an oracle is that we figured out how to stop it from having–

Toby Ord: Well, it differs. There was some early analysis of this at FHI, I think, where it was more being treated as if it was an agent whose goal was to answer questions correctly. I think that a lot of the problems remain, if it’s an agent who has just one type of action which is an answer, and it selects that action so as to have the greatest expected value, where the value comes from whether it’s rated as accurate. That maintains a lot of the problems of agents. What you’d ideally like is a system that is not choosing its actions based on consequences; it’s choosing its actions, in that case, based on truth aptness or something.

Arden Koehler: Can I return for a second to this question of uncertainty and what to do with it?

Toby Ord: Yeah.

Arden Koehler: So one way of pushing back on what you were saying is, “Well, if more uncertainty should actually oftentimes makes us more worried about something, or we shouldn’t at least start from the skeptical place, then”… I guess, I have this sense that somehow there will be too much to worry about in that case because what am I most uncertain about? Well, it’s all the stuff I haven’t even thought of yet. Or all of the developments that I don’t even know how they’re going to go at all. Really, you need some case there, at least, or something to constrain the explosion of concern.

Robert Wiblin: At some level it proves too much, because then you’ll be like, “Well, then we should just all be working on the thing that we know the least about”. So it has to be that we have some clues that it’s bad but then we’re missing other pieces.

Toby Ord: I agree with that. If there weren’t either this analogy in the case of AI to humanity and intelligence or intellectual abilities being so crucial in our power. If that didn’t exist, and if these arguments about why maximizing patient maximizing agents would have instrumental reasons to deceive us and wrest control from us; if those arguments didn’t exist, I would be a lot less concerned about this.

Arden Koehler: Yeah.

Toby Ord: Those arguments are quite old. You know, they’ve been rediscovered recently, but there are famous computer scientists making them last century.

Arden Koehler: I guess another thing you could say in response to this is just, “Well, in fact, those are the most worrying scenarios but the things you have literally no idea about, you’re just not going to be able to do anything about”, so it’s more of a tractability argument.

Toby Ord: Yeah, I guess so. But there is this challenge. It’s also a challenge in science, as to where do hypotheses come from? At the point where you’re entertaining all hypotheses simultaneously or something, there’s some craziness about trying to understand what’s going on there. Or, how do we do the bit where we, from that cloud of exponentially many ways of constructing a sentence that would describe something about the world, to actually picking one out? We do a lot of the work in actually even working out which thing to test, before we even try to test it. How does that process work? This is a famous unsolved epistemological problem in the philosophy of science. I think something like that’s going on here. Why do we focus on certain things as risks? But, I agree that one could make some kind of proving too much case, and that it would be interesting to explore that.

Robert Wiblin: All right. You have a bunch more about AI in the book, we should probably push on. Just very quickly, you have this one in 30 risk from other anthropic risks which I guess is the unknown, unknown stuff that people might make. How do you come up with that? I guess, this is, almost by definition, the one that you can’t say anything specific about because it’s the stuff that is that?

Toby Ord: Yeah, very unclear. The question is, I think, roughly why is it so low? And, why is it so high? There are the two types of questions.

Toby Ord: Why isn’t it lower is to do with thinking about how recently we’ve discovered a whole lot of these risks. And, if you imagine asking people equivalently, 50 years or 100 years ago, what would be the major risks over the next 100 years, that they would be in a very difficult situation in predicting what we now think are the greatest risks. It wouldn’t be totally impossible, but it would actually be very difficult. There are some attempts at this and they didn’t do that well. So, thinking in those terms makes me think that we shouldn’t say that it’s a super large fraction of the risk in the stuff that we currently we see versus the stuff that is unseen or unthought about. I give quite a large fraction, so it still ends up being pretty low.

Toby Ord: Then, you could ask some question about why isn’t it higher? Maybe I’ve got less ability to defend in that direction, actually.

Arden Koehler: Maybe it’s just the fact that it’s limited to the next 100 years, right?

Toby Ord: Yeah.

Arden Koehler: So if it was what’s most likely to cause an x-risk over the next million years, it would probably be the unknown, unknown. But, just because it’s a pretty short timescale.

Toby Ord: Yeah. I think that could be right. One thing that is helpful is I actually think there’s a decent chance we’ll start getting our act together on this in the next 100 years. So even if we can’t say exactly what the causes would be, that all cause risk will start to go down, rather than up. That may not be right, but I think there’s a reasonable chance of that.

Robert Wiblin: Maybe one thing is that you’ve covered computers; that’s the AI bucket. You’ve covered the life sciences; that’s the pandemic risk. I guess we have physics; that’s the nuclear things. It’s like, what’s left? For some conception of these things, they’re very broad, I suppose?

Arden Koehler: Killer philosophy.

Robert Wiblin: Right. Ideas, right? Or some terrible idea?

Arden Koehler: Yeah.

Robert Wiblin: You have this funny argument in the book which I find very satisfying, which is that whether you think the risk of extinction this century is high or low, that shouldn’t affect the value of working on existential risk. Because if the risk is low, then that suggests that the lifetime of humanity, if we manage to get through this century, is going to be very long, because in general, the risk of extinction is low. On the other hand, if it’s high then that means there’s a lot of existential risk, or a lot of risk of extinction to reduce, so it should be more tractable. On the other hand, that means if we do make it through this century, we probably will die out soon anyway. Do you want to explain this one?

Toby Ord: Yeah.

Robert Wiblin: It’s a nice little “gotcha” for people who want to be like, “Oh, I don’t want to work on it, because it’s not likely.”

Arden Koehler: He finds it satisfying; I find it suspicious.

Toby Ord: Okay. What’s going on here is that this is a very simple model of existential risk and existential risk reduction. The model here is that there’s some constant rate of exogenous extinction risk or something per century. Let’s say 10% existential risk per century. You can do work on the risk in your century, but not in other centuries, and it’s going to stay the same over time. So, that’s the model. This is the kind of model that economists would start with. One thing that’s interesting about it is that it doesn’t suggest that the work on existential risk is overwhelmingly important. On this model, it ends up being important, but not overwhelmingly so. I’m not helping myself here to a model which supports the strongest versions of the types of arguments I’m talking about. But, on that model, the expected lifespan of humanity is basically one over the risk. So if there’s 1% risk, we’ll last, on average, 100 centuries. If there’s a 50% risk, we’ll last, on average, two centuries. Even though you could be removing 50 times as much risk, the future that you save is a 50th the size. These things always would cancel out on that model.

Toby Ord: Then interestingly, if you extend the model, and you imagine that what you could do, instead of, say, halving, or eliminating the risk in your century, is that you could halve or eliminate the risk over all centuries. I think some work on existential risk is of that form, where it’s not just dealing with today’s threats, you’re actually fundamentally enhancing our ability to understand and manage this risk, or that there’s a limited number of such risks. But if you could be lowering it in all future centuries, then you actually end up with an even more surprising conclusion, that the lower the risk level is, the more important it is to be, say, halving it. Because if it’s currently 50%, and we’ve got two centuries of expected lifespan and we halve that, then we get four centuries. You’ve added two centuries of value. But if it was 1%, where you have 100 centuries of value, and you halve it, you get 200 centuries of value. So you’re adding 100 additional centuries.

Toby Ord: So you can actually get that kind of effect which is surprising to people. Most people, it seems, who are skeptical of working on existential risk, do so on the grounds that the risks are small. But they forget that means that the value is very high, of survival. It’s not just my opponents who are making strange kind of thing, my allies, typically argue that because the risk is high, that we should be working on it now, and there’s something perhaps going wrong there. But this can be partly resolved if you improve the model.

Robert Wiblin: Yeah. If you think the risk is getting higher century after century, then I guess a bunch of this might be reversed, right? Or, if it’s just inevitably that the risk is going to go up.

Toby Ord: Yeah. If the risk was inevitably, so unchangeably going to go higher, yeah then there’s a smaller future, and it’s more important if there’s more risk now. That’s right. Also, if you thought the risk was going to go lower, and that you didn’t need to do anything about it. Just it was going to go lower on its own, say, in the future. Then similarly, it would turn out to be more important if there’s more risk now.

Arden Koehler: It seems like people do generally tend to focus more on existential risk if they believe it’s high? It seems like they can’t just be making this mistake. So, what might be going on there? I was thinking, it could be something like the largeness of existential risk is a proxy for tractability? So, if the risk is really, really low already, that might imply that it’s hard to lower it still, whereas if it’s really high, that implies that you can take it down a lot?

Toby Ord: I think it would make sense to use the size of it as a proxy for, say, how many percentage points you can lower it by. If there’s 50% existential risk, it’s probably easier to lower it by half a percentage point, than if there’s only one percentage point of existential risk in the century. But, actually the argument I’m making, though, I was looking at the value of lowering existential risk by a given fraction. So, say the value of halving existential risk ends up, in the first case, being the same, no matter what the risk level is. And, in the second case, being more important for smaller risks. But, I think what is probably going on is that once you complicate this model a little bit more, and you allow this possibility that we’re in a particularly risky time, and that the risk might go down in the future, then I think that you do get the kind of intuitive result out of it. And, you also start to get overwhelming value of working on existential risk as well, because there could be a vast future. You get a realistic chance of achieving a vast future if it’s not exponentially diminishing.

Arden Koehler: So, if the risk is high now but low later, then you get both, the same direction from both of those, that says x-risk reduction is a higher value?

Toby Ord: Yeah, that’s right. That existential risk reduction is more important the more risk there is in our century. I think that’s probably right. One way to think about all of that… I’m not trying to be counterintuitive for the sake of it, there. It’s more, what if we start with the most obvious model? If we instead start with the model with lots of bells and whistles on it, a model that assumes that risk is going to be low later and various things like that, people might be rightly skeptical. But if we start with this very simple model, you still actually get the kind of conclusion that it’s very important to work on existential risk, but not that it’s overwhelmingly important. You get this conclusion, regardless of how much risk there is.

Toby Ord: That puts some pressure on people who say that low amount of risk would be a reason not to worry about it. But then, once you actually start making these complications to the model, in order to get the more intuitive starting point on it, it does seem to suggest that actually, yeah maybe the more intuitive models of this really are the ones that have enough bells and whistles on them such that the expected value of working on existential risk is extremely high.

Arden Koehler: I want to come back to the question of whether we might be at a particularly risky time right now relative to the future. Just to get clear in my head about this, it seems like it isn’t just easier to reduce a larger risk by certain percentage points, it might actually be easier to halve a big risk. So I’m thinking if you had a really high existential risk, it might be because we’re doing something really stupid. Or it might be because there’s some really bad situation and there might be low-hanging fruit there that you can pick and then you might even be able to cut the risk in half. It might still suggest greater tractability to have higher levels of risk?

Toby Ord: My guess is that halving it is roughly the right way to be thinking about it. Like a given proportional change being roughly equally easy.

Arden Koehler: Okay.

Toby Ord: With an exception being that if the risk is really high, like 99.999%, maybe that suggests that it’s overdetermined.

Arden Koehler: I see. That’s even harder.

Toby Ord: And that we’re in some extremely difficult situation and it’s harder. For the math students out there, I would suggest that you use something like log odds as your scale, where it’s hard to make large, absolute movements when you’re close to either probability zero or probability one. And easier when you’re in the middle.

The hinge of history [02:15:20]
Robert Wiblin: Okay. Let’s talk now about this debate about whether we’re living at the hinge of history which is a crowd favorite. So Will MacAskill, in my interview with him, I guess made a bunch of arguments to try to explain why, in his view, he thinks the probability of an existential risk within our century is under 1%. Yeah, did you want to respond to any of those? Or try to explain how you think it is that you and Will, despite working together, and knowing one another, and having heard all these arguments, end up in a different place?

Toby Ord: Sure. One thing to say is that the place we’re in is not all that different, and I thought it was a great post, and I was really excited to see it. As I think it’s an interesting challenge to these ideas, and the exact type of post I want to see. So, just to clarify that, we’re still certainly on friendly terms. Also, that his position is now a bit less extreme than it was when he wrote the post. Although, maybe where it was when he had the interview with you, where he effectively thinks that, what’s the chance it would be now, why not some other century? That he thinks that the prior chance that it would be this century is very small. He thinks that you can update quite an amount, based on the evidence that we have that we’re in a particularly important time, but he’s not sure how much you can update on that. He’s worried that if you perhaps thought that the expected number of centuries that humanity could live for were, say, a million centuries or something, because you’re taking seriously the possibility that we survive, say, until the end of the Earth’s habitability, or beyond. If you were thinking in those terms, maybe you’d say, “That’s a million centuries, so there’s only a one in a million chance that this will be the most important one,” or something like that. That maybe then it’s hard, based on the fuzzy evidence we have about our own time and all of the reasons we could be biased, it could be hard to then inflate that number up to a reasonable chance. So I think that’s an interesting argument. I think the main difference with my own view comes down to the choice of this prior, which is, I think, a fascinating question. There’s probably some people in your audience thinking, “Oh my God, not this again”.

Robert Wiblin: Yeah.

Toby Ord: But I do think that it’s very important, and I think that there’s a lot of importance about choice of priors when it comes to existential risk. This is an area, actually, we can afford to develop our expertise in. There’s this issue that, in science, usually the choice of prior washes out, so long as your prior includes some kind of probability for the truth, on the true outcome. If you get enough data, eventually the shape of your distribution converges to the truth. But, when it comes particularly to existential risk, we’re in a situation where we don’t have many examples of existential catastrophes happening. In fact, it’s not only unprecedented, but it’s necessarily unprecedented. It’s impossible for us to witness an example of humanity having its potential destroyed, before we have it destroyed. We can’t help ourselves to the usual scientific standards and things, and the choice of prior matters, and I think some choices are better than others. That’s why I think that matters.

Toby Ord: I think that you should almost never have a choice of prior where you’ve got a long interval, and you assign your probability uniformly across this arbitrarily long interval. That, in general, it should always usually be diminishing over that interval. So, there’s a standard issue there where if you try to say, “Pick a random real number. Any positive real number at random,” or something, there is no probability distribution that assigns an equal chance to every real number. Instead, you have to have a shape of a distribution that diminishes towards zero.

Robert Wiblin: Because otherwise it goes over 100% probability?

Toby Ord: Yeah.

Robert Wiblin: Even if it’s an infinitesimal for any one, because there’s an unlimited number of these numbers?

Toby Ord: Yeah.

Arden Koehler: Can you give a more concrete example of when you might think we should use a uniform prior, but in fact, that’s the wrong choice?

Toby Ord: Yeah. Well, I’ll go with my abstract example, first. So, there is no way of doing that. What you would typically do is a prior, such as an exponential prior, where it becomes half as likely to have a number one higher, or something like that, because there is actually a prior like that over the real numbers. So, if you’re doing it over the whole real numbers, that’s how you’d do it. Then if you say, “Suppose we know that we’re not going to live more than a certain number of centuries, we’ll cut it off there”. What we should do is have the prior that went all the way along and diminished and cut that prior and rescale it”, instead of now deciding that the bias towards zero doesn’t exist or something like that. So that’s a general point that’s pretty abstract. But, I’m very suspicious over these things with arbitrary intervals where they spread it out uniformly.

Toby Ord: But, on the particular case, what I think is that there’s an argument that Carl Shulman made explicitly that you talked about in that episode, where he was saying that a model where an earlier event could crowd out a later event. So there’s certain forms of ways that our century could be most influential, such that if it happened earlier, the later ones could no longer be the most influential because this has done the thing. That is what I’m thinking about. If you have a model where the most influential century occurring at some point crowds out it occurring at later points, you end up with this diminishing probability over time as to when it happens. If you started with a constant hazard rate, as they say. A particular chance, a constant chance each century that this is going to be the most important one, but once it happens, it crowds out the later ones. And you’re uncertain about what that rate is, then you end up with this Laplace’s law of succession type prior. On that prior, it turns out, particularly if you think of it in terms of the number of people who’ve ever lived, or the number of life years that have ever been, that about 5% of the people who’ve ever lived are alive now. In terms of what’s the chance that we live at the most important time, when 5% of the people who’ve ever lived are alive, it ends up being not that far away from one in 20, rather than one in a million, or something like that.

Arden Koehler: Just to try to make this a little clearer to myself, it feels like one of the fundamental differences here is that Will is thinking of this as the question of, “When will a certain sort of event happen over this long a period”?

Toby Ord: Mm-hmm (affirmative).

Arden Koehler: And you’re thinking of it more like, “When will an event first happen over that period”?

Toby Ord: Yeah, that is kind of right.

Arden Koehler: So, can you explain the reason that the second thing is the better way of approaching it?

Toby Ord: Yeah. So, as an example, if this was the century we went extinct, plausibly that would be the most important time in human history. And you only go extinct once. So that’s one way it could happen.

Toby Ord: If it was the century we went extinct, and there was nothing we could do about it, maybe on some measures, this wouldn’t be the most important century. But, it seems like there’s probably something we could do about it. Some kind of elasticity of this probability to our actions. Some way it would respond. So, I think that it would very plausibly be it. If you spread out the probability mass too much, as in your prior, if you say that there’s only a one in a million chance this century could be the most important, and you agree that if this was the century that we went extinct, that that would qualify, it proves too much. It proves that there’s almost no chance that we’re going to go extinct this century, just from consideration of the expected amount of centuries we could have, which was itself based on a guess about the chance of going extinct at different times, and so on. I don’t think that’s bottoming out properly, or something, there. It’s proving too much.

Arden Koehler: Maybe a way of saying this is, a large proportion of the events that would qualify a century for being the most important century in history are extinction events, and those are the kinds of things where, what we are wondering about them is, when are they going to happen first?

Toby Ord: Mm-hmm (affirmative).

Arden Koehler: Because it’ll crowd out all other later events.

Toby Ord: So, that’s one way it could happen, yeah. There are other ways I think it could happen that are related. So, if this was the time we achieve what I call in the book “existential security”, which means getting to a safe position, getting humanity to a point where we have the civilizational wisdom to not pose these risks to ourselves, but to take our time and caution when we develop new technologies, and to make sure that the risk is very low, and keep it low and live for a very long time if we got our act together. And, that if we were also very careful, and had what Will and I call the “long reflection”, really thought a long time about how best to fulfill our potential, that once we’ve achieved existential security, and were safe from these catastrophic threats of destroying our potential, we would then have enough time to work out how to actually fulfill our potential and then go and do it.

Toby Ord: So if we set things up like that, that would be the most important century. I think that there are reasons to believe that we could, sometime this century or the next few centuries, actually make those changes to how we govern our world. There are reasons to understand that. You might say, “Why didn’t that happen five centuries ago, then?” Well, part of the answer is, five centuries ago our world was a divided place. We’d only just crossed the Atlantic, and we were in no sense a global community, able to make global institutions for framing these things, whereas now we’re closer to being able to do it. There are some reasons to think that. It’s another related way in which one century being super influential would crowd out the future ones being so influential. And then, that’s a reason why you wouldn’t expect the chance to be evenly spread over time, but rather to drop off quite rapidly over time.

Arden Koehler: How important is it for this argument that this century has a decent chance of being the most influential? That you think it’s likely, or reasonably likely, that we’re going to enter a phase of existential security in the not too distant future?

Toby Ord: I’m not sure. The main case I make in the book is, I guess, not framed in terms of being influential overall. Will’s argument is attacking that broader target, which is great. But, I’m making a more narrower case that it’s an extremely important time because of the levels of existential risk that we’re facing at the moment, rather than necessarily the chances of existential security. I was just showing that there were other ways, or related ways, of making the argument. And, that if you have any real credence in any of those, then your probability distribution… If you have a mixture, right, if you say, “Okay, I’m 90% sure of Will’s model, 10% sure of Toby’s model.” Then you mix these priors together appropriately, you end up with very macroscopic chances, just a 10th as high as mine, basically, of the early times being really important. So, instead of it being one in 20, it’s one in 200, but it’s not one in a million. I think that so long as you take this kind of seriously, then it does this. But we’re getting very abstract and maybe I’ve made some mistake here, or something. I think this does warrant more continued public discussion.

Robert Wiblin: Yeah. I really hope that someone’s going to do a very comprehensive survey of all the different prior options and try to figure out what it really is, because this is very important stuff. It feels like we haven’t exhausted all of insights here by any means.

Toby Ord: Another case just to show how this can be important. In the case of climate change, I mentioned before the sensitivity number. Like, if you doubled CO2 concentrations in the air, what would happen to the temperature? The IPCC say there’s about a one in six chance that it would go above four and a half degrees of warming. But what about the chance of it being 10 degrees of warming, or 15 degrees of warming, or something like that? Wagner and Weitzman wrote this nice book on this, and they did a form of estimation of that, where they modeled it as log-normal distribution, this probability distribution. But really, other people have tried other things, like a normal distribution, a uniform distribution, between zero and 20 degrees of warming, and various other things. Then, some further work showed that the answers you get all depend on the prior you put in. And partly that was said, I think, in this traditional science way of shutting up these people or something that, “Well, you say there’s a one in 1000 chance of 10 degrees of warming, but that’s just because of your assumptions.” That’s a fair point. But, I think more alarming, or the real thing to get out of that is that the tails of this distribution, like what is the chance that we get really large amounts of warming if we double our CO2 concentrations due to feedbacks are just not constrained by the data at all.

Robert Wiblin: Yeah.

Toby Ord: The fact that it’s entirely dependent on the prior is very alarming. I think some of these priors that are considered are actually pretty plausible, like power law priors, or log-normal priors, and we should actually take them seriously. But that’s another interesting case where choice of priors ends up being very relevant to discussion about existential risk and modeling of extreme climate change.

Toby Ord: I think there are a lot of cases like this because we, again, can’t get that much evidence. In order for humanity to overcome every existential risk for the whole future, we need to get better about reasoning about cases before something’s happened 1000 times. I think that that study of doing that is in its infancy, and will be a good thing to push along.

Robert Wiblin: Yeah. If I recall, in the comments on that blog post, which I know we’ve talked about quite a bit, we might be getting a little bit in the weeds. So Will suggested this uniform thing which everyone agrees isn’t exactly right, but as an illustration. Then you suggested, I think, the Laplacian prior, as an illustration of the alternative. I think some people objected that that had to be going too far in the other direction, because that was placing too much weight early on. It would suggest that it’s almost certain that the most influential century in human history would be extremely early and it almost certainly would have already happened. Am I understanding that correctly? So it has to be something a bit intermediate?

Toby Ord: I think that is the best objection: is that my approach gives pretty good results, pretty plausible and intuitive results looking forwards, but gives some pretty weird results looking backwards.

Arden Koehler: I don’t know. I’m not sure that’s that great of an objection, because–

Toby Ord: Well, thank you.

Arden Koehler: Well you might think maybe we should just think it is very, very plausible that the most influential time in history has already passed. But obviously, our real question wasn’t when is the most influential time in history, it’s when is the most influential time in the future?

Toby Ord: Well, I still take some of the force of it, because if you just apply it naively, it does end up saying that the chance was 99.999% or something that it happened in the past. I actually don’t believe it happened in the past. If I did believe it happened in the past, I could retreat to saying, “Yeah, okay, but we’re only concerned about the future that we can affect, so I could use your argument. But, I’d feel a bit suspicious in doing so, because–

Arden Koehler: Because you don’t think it happened in the past. But, why not? I mean, you might think we have these really small populations. Things could have gone this way, or that way. We might not have even evolved. I don’t know, it seems like all kinds of ways in which it could have happened in the past?

Toby Ord: I guess if I was thinking about a different world. Like I heard there was another planet with an intelligent species, that had evolved. I wouldn’t think that my view is too unreasonable, like as in this Laplacian prior. I wouldn’t think, “Oh well, they’re definitely going to have to go through 200,000 years before they start posing risks to themselves”. I don’t know. Effectively, I think there was some kind of scaling up thing. You can think of it as dampening the start of this prior. So the prior is this hyperbolic distribution over time and it starts high, and goes low. But then there’s also another effect which is our power, or our ability to actually affect anything over the future or something that maybe started low and got higher. And that you have to multiple these together and you end up with something that starts low, goes high, and then goes low again.

Toby Ord: But, there’s uncertainty about when is the peak? Quite wild uncertainty about that. Maybe there’s something like that going on, but I know that at that point… The virtue of my model was that it was so simple that I wasn’t rigging it. Now, I’m starting to put stuff in it based on what we know that sounds a little bit like I’m rigging it. So I’m not sure.

Robert Wiblin: Maybe you could save it a bit by indexing it by population rather than time. I guess another thing is you could just say, “Well, it’s totally possible that the most influential century was in the past. There’s various examples we can give. But 99.9% sure? It doesn’t seem like we’re completely committed to some path, so it can’t be quite that far.”

Toby Ord: Yeah. I mean, I think–

Arden Koehler: You wouldn’t have to be completely committed to a path in order for that to be true. It would just have to be that the biggest chunk of the space of possibilities had been already carved off. I guess, I think, we already are probably in a much smaller space of possibilities than we were–

Robert Wiblin: A million years ago.

Arden Koehler: A million years ago. We could have been anyone.

Toby Ord: Yeah, I would be interested if you tried to develop that, the view that the most influential time has already happened. I mean you could see how some of it could have happened.

Robert Wiblin: Well, it could be the start of Christianity, say?

Toby Ord: So yeah, Will’s looked into this, the “Axial Age” as it’s called, where a lot of these religions developed.

Robert Wiblin: New paper suggesting that doesn’t exist, by the way.

Toby Ord: Oh, yeah?

Robert Wiblin: Sorry, carry on.

Toby Ord: Well, that would help with this argument. Or, it could be that it was, say, 150,000 years ago, when all of the humans were still in Africa, or maybe there were pivotal events there that were very important and we could have all died out then or something.

Arden Koehler: Also, there wouldn’t have to be the possibility of existential catastrophes for them to be the most important events, right? It could be the fact that we opened up this big future by developing in certain ways?

Toby Ord: Well, I think that that future has always been open or something.

Arden Koehler: Okay.

Toby Ord: In the sense that I’m talking about. The idea of the potential of humanity is a key idea in the book. What I’m thinking about there is the space of all possible futures that we could ever create. That’s the sense of potential and the value of the best ones that we could reach. That’s the sense of potential that only ever gets smaller. You could have other useful senses of potential where you develop industry and that gives you the potential to do new things. But that’s a kind of local potential. It gives you the potential to do them in the next 10 years, say. But if it’s the potential to ever do them. To ever reach that point in this space of trajectories or something; that’s the kind of potential that only decreases. Since I currently think that it’s possible that we achieve basically zero, or that we move to extinction soon or something. And I also think it’s possible we achieve something closer to the top. I think that they’re both reasonably possible. Then, I think that commits me to thinking that it’s not the case there was a pivotal event a long time ago in the past.

Robert Wiblin: Okay. So, a different line of argument that Will brought up was that there’s eight billion people now, so many people, and almost nobody wants everyone to die. Governments are maybe not the best institutions that they conceivably could be, but nonetheless, they kind of function. Surely, if it was imminent that everyone was going to die, people would put in the effort to prevent it from happening. So much effort would go against this death, how is it plausible that everyone would be killed? What do you think that line of argument?

Toby Ord: I think that it’s helpful. As in this is a reason that would count in favor or something happening about it. I think that there a whole lot of reasons to suggest market failure, whereby the governments put in a tiny fraction of the work that they optimally should put in. For example, say, in the UK, where we are now, has about 1% of the world’s people in it, and so if we do something to lower existential risk, we’ll only recoup 1% of the benefits for British citizens, who are normally the people they’re talking about when they’re doing their budget. So, that’s a reason why they might under-invest by a factor of 100. Then, when you consider all the people in future generations, only a tiny fraction are around now. And together, these suggest that there’s a big market failure, where we might put in only a tiny fraction. But, you might say, “It’s still big enough though that we’d really try”.

Robert Wiblin: It would be sufficient, yeah.

Toby Ord: That could be right. I’m merely claiming here that we’ll undervalue it by some immense factor. I’m not claiming that we won’t still find it sufficiently important to act on it. But I don’t find that compelling that there’s no chance that we’ll… I mean, just look at the current issues, like climate change, and things. It’s possible to be all well aware of what some of the actions we need to take are, such as either a carbon tax, or carbon trade, and then just be floundering around in decades, in terms of, “You go first.” “No, you go first.” Or, to say, “We should do it based on going emissions,” versus, “We should do it based on historical emissions”. Or, “We should do it on a per capita basis”, versus “Not a per capita basis”. Or things like that where it turns out to benefit one country or another and so they keep arguing about it.

Toby Ord: And that’s on something where the aspects about carbon emissions causing climate change is fairly cut and dry, whereas on some other issues, such as artificial intelligence, and whether, say, artificial agents have a tendency to want to control the future based on the fact that they have a utility function or something. It’s getting pretty abstruse, and I’m just not sure that this is the kind of thing that I’d expect to be well managed by the world’s political processes.

Reasons for optimism [02:34:34]
Arden Koehler: Okay. So earlier you said that your argument that reducing existential risk is really important doesn’t require thinking that risk is going to go down anytime in the near future, but if it is going to go down anytime in the near future, that really makes reducing existential risk now extra important because it increases the value of the future. You seem relatively optimistic that we’re going to reach a state of existential security in the not too distant future, maybe in a couple hundred years. But, I’m not really sure what the reasons for optimism are. I would think that, well, existential risk has been going up so far, it seems like there’s this pattern where we get more power, there’s more risk. Why should we think that’s going to reverse?

Toby Ord: Yeah. Carl Sagan, when talking about this stuff in the ’80s, when he realized these risks, he had some great conceptual work on this that’s very similar to the work done by Derek Parfit. He attributed this to humanity growing powerful without growing commensurately wise. I think that’s a pretty good way to look at it. That it’s not the case that it’s just an argument that we shouldn’t have high technology because high technology will doom us, so we should be Luddites. But rather, you need to be aware of these fresh responsibilities that come with these new levels of power. And that we’re capable of growing our power exponentially on a lot of metrics. But there aren’t many metrics where we’d say humanity’s wisdom, or institutional ability has been growing exponentially. We generally think it’s faltering, if at all. So, he sees this as this problem, and I kind of agree. He calls it a “Time of Perils”. I call this time, “The Precipice”. A time where we’ve reached the ability to pose existential risk to ourselves, which is substantially bigger than the natural risks, the background that we were facing before. And this is something where I now think that the risk is high enough, that this century, it’s about one in six.

Toby Ord: So I think that there’s a time period, The Precipice, that can’t go on for all that long. One of the reasons it can’t go on for all that long is if the risk keeps increasing, or if it stays the same, then you just can’t survive that many centuries with a risk like this. That changes a bit depending on how much risk you think there is now. So you might think that the case for existential risk is still really strong and important, but there’s only 1% risk. But therefore the time period could go on for a very long time, perhaps. I think that it could only go on for a handful of centuries. So it’s a bit like thinking about something like the Enlightenment, or the Renaissance. Some kind of named time period like that is what I’m talking about. I think that the risk is either going to go higher, or that we fail out of this time period. Or, that we get our act together and we lower these risks. So, on that issue of lowering the risks, why do I think that’s likely?

Toby Ord: I think that the arguments are actually just pretty clear and compelling as to why we should do this. I think there’s very strong moral arguments, and they haven’t had much of an erring yet. I think that if we look back historically in the 20th Century at things that were not part of common sense morality, such as animal welfare and environmentalism, they very rapidly grew to a very large amount of attention and they became key parts of what we think of as morality. To the extent to which a lot of people just judge other people, whether they’re moral, by whether they eat meat, or whether they do recycling, or whether they care about the environment. These are touchstones for how people think about moral action now, and they were not almost all of human history. I think that these arguments currently seem like a strange thing to focus on as a core part of morality, but I think that there’s a good chance that we will.

Arden Koehler: So, your examples of the environment and animal welfare, if anything, to me, make me more worried. So there are these clear arguments for why factory farming is really bad. For why climate change is on the horizon and human-caused, and yet both problems are getting worse. Even though more and more people care about it, there are these really strong incentives that are keeping us from doing that much about it. So, you might think that’s a reason to worry that humanity won’t get wise?

Toby Ord: It could be. I think that it depends on where in the world you are. So these things are scaling with economic productivity, but they’re actually often going down relative to the economic productivity. So, for example, the UK has continually improved its standards for farmed animals. The UK has also decreased coal use to the point where we had some time over last summer where there was no coal use at all. It’s a negligible fraction of the energy portfolio of the UK. And carbon usage, I think, from the UK and EU is going down. Within 10 years of the environmental movement starting, there was a Minister for the Environment in all anglophone countries except New Zealand, I think. I think it is a case where you could treat this as pessimism, but I think that it’s not skating to where the puck is going.

Robert Wiblin: It’s a mixed picture, I guess. One thing is, there’s a whole lot of environmental issues and the reason we’re talking about climate change is that that’s the one we’ve struggled with the most, and that’s the one that’s still here, whereas many others we’re fixing.

Arden Koehler: That’s true.

Robert Wiblin: With the animal thing, there’s definitely more animals suffering in factory farms every year. But, from another perspective, every year the technology for clean meat and for meat substitutes is getting better, bringing us hopefully closer to the day when it would be completely obsolete.

Toby Ord: I imagine the proportion of vegetarians has been going up?

Arden Koehler: It’s been oddly flat, actually.

Toby Ord: It’s been oddly flat? Okay.

Arden Koehler: Yeah.

Robert Wiblin: Yeah.

Toby Ord: That’s interesting. But I do think that these are cases where, at least they get halfway to the argument, which is that you can have things that become part of common sense morality within a generation. Particularly if they were issues where there was little we could do about them, or the issues weren’t really there a generation earlier, and that humanity, over that time scale can learn and adapt and incorporate these things as part of our way of doing business in the world. But then you’re right that it does raise a second challenge, which is what’s the chance that the moral things actually win the day and determine our cause of action? But at least you can see how I could think that this is at least plausible.

Toby Ord: Yeah, I also think that there’s a strong democratic critique of our disenfranchisement of future generations. I think Will’s going to be making this very forcefully in his upcoming book. I think there’s strong political theory reasons as well, and if you look at other cases of enfranchisement of different people, I think there’s quite a few sources for hope about this.

Arden Koehler: So, it seems like your answer is you have some reasons to be optimistic?

Toby Ord: Mm-hmm (affirmative).

Arden Koehler: But then, you also say that if we’re pessimistic, and we think the risk won’t go down in the near future, then that’s not a world where we can save ourselves very well anyway, right? If we’re going to continue at some large degree of risk, then even if we get through this century, we’re not going to have most of humanity’s potential in the long-run anyway? So it’s kind of like you might as well focus on the cases where you think existential risk is going to go down in the not too distant future?

Toby Ord: That could well be right. It’s not a central argument in my book.

Arden Koehler: Okay, sorry. That’s what I thought you said.

Robert Wiblin: That’s an argument that I was making the other day.

Arden Koehler: Oh.

Robert Wiblin: Let’s say there’s three different scenarios. One where the risk is just going to go up very likely unless we do some unbelievably high effort. The other, it just stays flat, and the other, where it goes down. So you place one third probability on each. The first is a write-off if you’re in that world. Just to almost ignore it. The second one, well, then we have a medium-long future, so we have these medium-strong reasons to reduce existential risk. The third one ends up dominating the whole equation. So as long as you place some initial probability on it, the longer you go out, the more it is just the case that, well, the reason you’re still around in 1000 centuries is because you’re in that scenario, because that was the most likely one.

Toby Ord: This is closely related to Martin Weitzman’s approach to discounting when you’re uncertain about the discount rate.

Robert Wiblin: Yes.

Toby Ord: In your example, you think that there’s maybe, in some sense, the future is being discounted in terms of probability. The probability we even have a future. In one case, perhaps by 50% every century. There’s hardly any chance we survive for a long time. In another case by, say, 2% per century, we’ll only survive about 50 centuries, on average. In another case by, say, one in a million per century, and we’d survive for a million centuries, on average. That third option ends up dominating things much more than it’s probability would suggest. The expected value, for example, mostly comes from that third option.

Arden Koehler: I think another way of thinking about this point is what are we going to do with all our resources if we don’t devote them to existential risk reduction? It’ll be other good things, maybe helping animals, or things like that. But, I suppose, you might think many of the best impacts of those other good things would end up being wasted, if we were in a world where existential risk stayed high or went up. So it’s not really possible to reallocate your resources in that world in a way that’s going to be super impactful.

Toby Ord: I guess this would be an argument between existential risk, focusing on existential risk, or other longtermist approaches. So thinking about this kind of long-term value that’s created by investing in things now, and they’ll come up there. If you’re more focused traditionally, say, on animal welfare, it’s not as clear that there’s a good longtermist argument for that, rather than a different approach where you say, “Actually, I reject the basis of longtermism, I think we should focus on things now.” If you’re going for that approach, then I’d think that the argument doesn’t quite work to say that existential risk dominates in some way.

Arden Koehler: Yeah, I think that’s right. Sorry, animal welfare was a bad example. I think I pulled it out just as a thing that we might spend our money on. But, you’re right, it has to be something that we think is going to have these really long-term effects.

Toby Ord: Yeah. That’s an example that would depend on the absolute level of existential risk, as to how long you’d have to compound those things otherwise. I make no claim that people should stop working on short-term ways of helping people, or that they should stop working on other longtermist activities. I think one of the strengths of effective altruism is that we have, whatever approaches we take to these things, and we can have some vigorous and interesting debates about which ones we should be doing, but still, we’re aware that there’s a lot of common tools and ideas and things that we would have going forward and that we should work together.

A vision for how the future could go well [02:44:01]
Robert Wiblin: Okay. I want to spend at least a bit of time on the last third of the book, which is trying to paint a vision for how the future could go well. Not just thinking about the risks that we face today. I guess, it’s written in a much more elegant and poetic style than I think I could ever write in. Or, I guess, than most books on this topic are written in. Because as you say, it’s like most of these things are written from a very engineering, “sciencey” point of view and you’re trying to, I guess, appeal to a broader audience by writing in a style that books are normally written in. You paint these quite vivid pictures of different ways that the future could go extremely well, I guess, to try to inspire people to care about them more?

Toby Ord: Mm-hmm (affirmative).

Robert Wiblin: There’s this funny way in which a lot of the visions are quite conservative. There’s this one part where I imagine that the sun is expanding and the Earth is doomed because it’s just going to get too hot and the oceans are going to boil away. Humanity decides to carry the biosphere to another planet, say, or go and recreate the Earth somewhere else. It’s just hard to imagine a more conservative vision for how our future could be that instead, we just want to continue with the Earth as it is today. You do mention there’s ways that the future could be very wacky. But, I suppose it just seems like, on it’s face, that the best future, surely, is very different than this thing that we just happen to randomly end up with today?

Toby Ord: Yeah, that’s right. There’s a few things I’m trying to do in that chapter. One of them is to try to give people some taste of what inspires me going forwards, and how great the future could be. I try to do that in a couple of different ways. One of them is to sketch what I call the shape of our potential. So, I look at how long we may be able to survive. How broad our civilization might be able to be in reaching other stars, or perhaps even other galaxies across the Universe, and just how much scope there could be. In the same way that you look back and you imagine someone on the hills of Rome founding a fledgling village or something and then thinking about how much their civilization could affect now. To try to give us some of that perspective.

Toby Ord: Then also thinking about, for a given amount of time and a given amount of space, how much better things could be, day-to-day, in terms of the quality. So I try to look at these three different dimensions, in order to sketch something about the overall shape of the possibility. Which you could think of as how much canvas is there for us to paint some masterpiece on? Then I try to sketch, also, a few examples within it of the kinds of things that we could do where they’re more lower bounds. So, we could at least do something like this. It doesn’t actually seem to require that much more technology than we have now, in order to do X, or Y, or Z. In that sense, it is quite conservative.

Toby Ord: In particular, I didn’t want to be just making random predictions of the kind of thing that after thinking about this stuff for 20 years, that I happen to believe might be likely, because I didn’t think that would really take the audience with me, or that I could really do justice to them. So instead, I wanted to focus on the types of things that we have actually pretty solid arguments for how long we could last, or how far we might be able to reach, or the types of things where we have pretty good lower bounds to what we might be able to achieve, rather than getting to the nitty-gritty of particular, exciting future scenarios.

Robert Wiblin: Yeah.

Toby Ord: I also wanted to avoid… Again, it’s like the two cultures things. If one tells stories, and this often happens with the transhumanist thought on the future: tell these stories where things are shockingly different.

Robert Wiblin: It’s hard to relate, maybe?

Toby Ord: It’s certainly hard to relate, but it also repels a lot of people. They think, “Well that just sounds terrible. Like, I don’t see that that future has any value. It seems so alien to me, that I’m shocked and alienated from the future”.

Toby Ord: And what I want to stress is that we don’t have to create a world that’s shockingly alien if we don’t want to. If we think that that’s worse, we shouldn’t do it. So, a lower bound should be a world that we can relate to and we think is a great continuation of humanity where we, say, commonsensically excel on all kinds of dimensions. We have better art, we have better culture, we have happier lives and richer friendships that are less marred by untimely deaths and other problems. So to paint something like that. To show the lower bound of what we could achieve. And then if things could go even better than that, maybe by transforming humanity into something new: all the better. But we don’t have to feel forced into that. So I wanted to take it a bit slowly on that.

Robert Wiblin: Yeah. And I guess the argument doesn’t rely on that. Yeah.

Toby Ord: That’s a key aspect, as well. That it doesn’t rely on it. And I find that if you sketch very, very radical changes to the future, they’re treated as very outlandish by people who haven’t been following the technologies of genetic enhancement or something. They just assume that your argument depended upon this thing that you mentioned, because you mentioned it and it seemed really unusual to them–

Robert Wiblin: Even though it’s a mere flourish.

Toby Ord: Yeah. And so I was trying to avoid that issue as well.

Robert Wiblin: Yeah. I wonder how much it matters, because in my mind, it’s just so clear how amazing the future could be that it could just produce amounts of value beyond our imagining, and it would be so much better than the world today. Perhaps I just assume that that’s a common belief or that’s a background assumption for me that’s actually perhaps quite rare.

Toby Ord: It is not a common belief in the world at large.

Robert Wiblin: I see, yeah.

Toby Ord: People have very divergent views on this and I think that the dominant view in our time is of–

Robert Wiblin: The future will be rubbish.

Toby Ord: Things getting worse. Yeah.

Arden Koehler: People might also just be so radically uncertain about the future, that they feel it would be unduly optimistic to think about these good scenarios when it could get so bad.

Toby Ord: Yeah, and that could be right. What I’m trying to do here is also not sketch necessarily the most likely future, but to show you the shape of our potential. What we could achieve. And the way I put it in the book is that we could divide up things, this grand strategy for humanity, into these three different phases, where the first phase is achieving existential security. And then the next phase would be working out what a great fulfillment of our potential would look like with a long reflection, which could be as long as it needs to be. And then, there’s the phase of achieving our potential. Actually implementing this plan and having this great future. And I think that while you could start working on some of these other things now, this is the only time you can work on securing the future. And so I think it really is the task of our time and we can leave to the next generation some of these questions about what really would be an optimal world were we free to build it, and things like that? That’s why I don’t want to get somehow caught up in that, and then end up having all my conversations with critics about what I said about that or something when it’s not central.

Robert Wiblin: Yeah, it makes sense.

Arden Koehler: So I’m curious about this second stage: the long reflection. It felt, in the book, like this was basically sitting around and doing moral philosophy. Maybe lots of science and other things and calmly figuring out, how can we most flourish in the future? I’m wondering whether it’s more likely to just look like politics? So you might think if we come to have this big general conversation about how the world should be, our most big general public conversation right now is a political conversation that has a lot of problems. People become very tribal and it’s just not an ideal discourse, let’s say. How likely is it do you think that the long reflection will end up looking more like that? And is that okay? What do you think about that?

Toby Ord: Good question. So, when I paint this grand strategy, what I’m doing there is something I look at a few times in the book, is what I call the “perspective of humanity”, which is adopting this perspective that’s even beyond the global perspective. It’s looking at not just everyone alive today, but everyone alive from the whole of the past and the future of humanity. And if we were thinking as a group agent, if we’re coordinating and acting together, what would we do? And so I think on these grounds, what we would do is we’d first put out the fires and work out how to install fire alarms and sprinklers and so on to ensure that we were never at risk of any other fires. Then we would work out how to use our resources in a really good way. And then we’d go about using those resources in that way. That’s just the means-ends rationality of the whole situation that I perhaps talk about more poetically than that in the book. But if we had our act together, how would we do it? But there’s serious questions about, well in practice, how will things happen and how much of a challenge will there be in having the reality be anywhere close to what we could have done if we were coordinated on this?

Toby Ord: I think that that is a real challenge, and that there would be fights fought about this and so on in order to get close to that. And I do think that often you don’t want to be taking this perspective of humanity. I think it’s neglected and has been done very rarely and should be done more. But it certainly shouldn’t be done all the time. Often you should be focused on how can we change things at the margins. Or how are the differences between people. Or disunity: how is that relevant to the situation? And that can be very important. But I think that this perspective of humanity is neglected. So I’m mainly adopting this perspective in this context of, well before we just go and do something with the universe, we should spend quite a while working out what that thing should be, given that it may well be not possible to revise those choices, but before we do that, we should actually get our house in order.

Toby Ord: So, that’s a fairly obvious progression. But I think that the political discourse these days is very poor and definitely doesn’t live up to the kinds of standards that I loftily suggest it would need to live up to, trying to actually track the truth and to reach a consensus that stands the test of time that’s not just a political battle between people based on the current levels of power today, at the point where they’ll stop fighting, but rather the kind of thing that you expect people in a thousand years to agree with. I think there’s a very high standard and I think that we’d have try very hard to have a good public conversation about it.

Robert Wiblin: What do you think is the most likely impediment to humanity deciding to actually engage in some kind of reasonable reflection and then acting on the philosophical and moral conclusions that come out of it? I guess there could be market competition that makes it hard or perhaps just people have intractably different values and they can’t reach agreement. Yeah. What worries you?

Toby Ord: Yeah, I mean, both those things. I think that it could be the case that there is intractable disagreement. For example, if the right way to think about ethics is not so much that there is some best moral theory that’s correct. But rather that it’s something to do with–

Robert Wiblin: What you like.

Toby Ord: Yeah, what you like or something. Then you’d expect there to be intractable disagreements, but you may still be able to get the best achievable compromise between those. So, the point of the long reflection is not to achieve the impossible. It’s to achieve the best possible within the constraints of how things turn out. But whereas the discourse being conducted in a way that’s not conducive to the truth anyway, or not conducive to best compromises, is definitely a bad thing and you’d have to go to a lot of effort to stop that.

Toby Ord: I think that this may be plausible though. In particular, the conversation is already starting, right? People do talk about what could be the ideal future, and so on. And they’re having these conversations more actually among moral philosophers and authors and people who want to spend time thinking about these things: public intellectuals. And it’s not currently being fiercely fought over. It might be that once we realize that we could implement these things that it will be fiercely fought over. But there probably at least be a while building up to that where it’s not being fiercely fought over and where there’s a space where there’s not too much noise. There’s a bit of quiet in which people can actually have these conversations in a thoughtful, careful way.

Toby Ord: But it’s also not enough that we just try to have a lovely conversation where we all feel really good about ourselves and we didn’t hurt each other’s feelings. We certainly shouldn’t be trying to hurt each other’s feelings, but we also need to actually find the truth, or the closest thing to truth that there is rather than just stroke our own egos and have a really friendly chat. And it’s challenging to meet all of these constraints.

Arden Koehler: I guess these issues bring up another existential risk that wasn’t the focus of the book and I don’t think we’ve talked about very much on the podcast, which is that we manage to survive and then we just do the wrong thing with our future. We just make the wrong choice about how we should spend the rest of humanity.

Toby Ord: Yeah. So I don’t end up classifying that as an existential risk. It would be if there was something that could be, in some sense, equally bad as an existential catastrophe. But, the way I’m defining an existential catastrophe is when our potential gets destroyed. And this would be a situation where our potential was never lost. We just carry on. There’s no irreversible moment. We just carry along a bad path, and for millions of years while we could have turned back, we never do, or something like that.

Arden Koehler: Yeah, I guess at the end we will have lost our potential, but it would be very slow.

Toby Ord: Yeah, but it wouldn’t be anything a normal person would call a catastrophe.

Arden Koehler: Yeah.

Toby Ord: It would be a trickle, or something like that.

Arden Koehler: Right.

Toby Ord: It’s just dripped away. And that could be how it goes. With a whimper rather than a bang. But, I would call that something else: failure to achieve our potential. And I think that the virtue of the definition, it would be even nicer if it included all such cases or something, but they’re quite different in some ways. And what the other ones have in common is that they’re relatively sharp moments, and then the methodology would have to be much broader and more nebulous if it was supposed to include these very different kinds of things. So I think there are some reasons to use the definition as is. But a case that’s somewhat similar that we didn’t discuss here is when I’m thinking about dystopian outcomes, that would be a whole extra podcast of getting into these types of details.

Robert Wiblin: We can do that in 2022.

Toby Ord: But I think that there are these other kinds of possibilities, which I only sketch in the book, where, rather than collapse or extinction, civilization continues on, but it continues on in a way that achieves almost none of the value that we could have achieved. And that in particular, is an existential catastrophe because it is in some way locked into doing so. So, for example, that a small number of people are having pretty good lives but are oppressing most of the people. And so, we end up with a very small average value compared to what we could have got before and that that’s locked in by various institutional mechanisms to do with advanced technology. We may not currently have the technology to lock in such an oppressive system, but maybe in the future with genetic engineering and sophisticated lie detection or things, that maybe that would be possible, or extra surveillance. So I look briefly at ways that things could get locked-in socially. And because they would actually within, say, a century, destroy the potential of humanity, those would count as existential catastrophes.

Arden Koehler: Because the lock-in would be a relatively discrete event.

Toby Ord: That’s right. It would be the lock-in which is the catastrophe.

Robert Wiblin: Yeah. I guess it’s interesting that we all focus a great deal on the extinction risk, the catastrophe risk, but I guess I feel it’s almost equally likely that we get through all of that, humanity continues, and then we just decide to do something incredibly lame or something that’s just so far away from the very best future that we could have made. That just seems much more likely than not. So, it’s maybe a little bit funny that that scenario doesn’t get a bit more attention. I suppose its getting attention inasmuch as you and others are painting this picture of the great reflection as a way of addressing that and reducing the probability. But perhaps it just adds more focus.

Toby Ord: Yeah, that could be right.

Robert Wiblin: I guess one thing is maybe that can be left to the future. This is the time when we can stop nuclear war, but–

Toby Ord: That’s how I’m thinking about this. I think that this is a convergennt strategy here as well with a lot of things where some people will, for example, have said, “Hey, in ethics there’s perhaps possibilities of creating infinite value or various other very unusual scenarios, and maybe we should be focusing on that and maybe it’s a rival to existential risk, say”. I think that we don’t know currently what to say about such situations within theoretical ethics. But there’s still this convergent approach where, if that is possible, we’ll have much more chance of achieving it if we survive this time. Then we’ll have a huge amount of time in order to achieve infinite value or whatever the other thing is that the person was discussing, and so it ends up being not so much a rival to this as part of what you’d solve in the long reflection.

Robert Wiblin: Yeah, Howie was suggesting earlier today that science fiction authors could be doing much more important work than is realized. One, because they open up people’s minds to consider that the future could be very different and perhaps much better than life today. And there’s so many dystopian books, but you could also make science fiction that makes people more hopeful about the future and motivates them more to improve it. But yeah, also I guess that it allows people to consider a broader range of possible futures, including ones that might be vastly better than what we might create otherwise.

Toby Ord: I completely agree with this.

Robert Wiblin: Yeah.

Toby Ord: It is in some ways shocking how important areas of human thought we have left to the science fiction writers. Many of whom do a very bad job of it. Some of whom do a fantastically good job of it. And there’s enough of those to be a lifetime’s worth of reading, just among the very good ones. And so I think that they may be tremendously influential.

Policy recommendations [02:59:49]
Arden Koehler: Okay. So, should we talk about things that maybe people should do? How we should actually proceed? You have some policy recommendations at the end of the book that I wonder if it might be worth just mentioning.

Toby Ord: Yeah, so I have a whole collection throughout the book, and then I collate them all at the end, of research and policy recommendations. Mainly research recommendations. Mainly to do with finding out more about the most extreme versions of a lot of these threats. Where some of these things have been studied quite a lot of the usual case, say, climate change, but very little about the most extreme cases, and recommending more research on those. Often, if I found in the course of writing the book, particular extreme unknowns where a lot of it hinged on that unknown, I’ll make sure to keep it in these lists, so they could be really interesting places for some of your listeners to see if they’re the types of problems they might be able to address in their careers in the research area.

Toby Ord: When it comes to policy recommendations, I’m quite a bit more uncertain because it’s very easy to create bad policy. As in policy that would be actively bad. And even easier to create policy that it’s not really policy. It’s the thing an academic thought was policy and they said we need to be more like this.

Arden Koehler: Policy compared to doing the research.

Toby Ord: Yeah. Slightly practical recommendation of some sort that actually no government could take ownership of or implement. And so I was aware of that and also aware that a lot of people who diagnose a really big problem, maybe correctly diagnose it, or really spell it out, they often then spend much less time picking the most obvious solution and then promoting that. And even when it’s actually not a great solution. And I wanted the book to stand the test of time, so I was a bit cautious about making too many such recommendations. So, they’re mainly things that are not that outlandish, such as, for example, renewing the new START disarmament treaty that’s about to lapse between the US and Russia or renewing the INF treaty.

Robert Wiblin: Those are crazy suggestions, Toby.

Toby Ord: Which they let expire. Or doing more R&D on clean energy and things like that. So I do make some of these obvious recommendations, and I also make some things that are maybe a bit more surprising in some way but, for example, ensure that DNA synthesis is screened for dangerous pathogens. That’s something that some of the companies who can create DNA, you send them the genetic code and they send you a test tube with stuff. Some of them screen it for whether you’re creating dangerous pathogens, some of them don’t. Hopefully we can get that to all of them screen it. If we can’t, we probably have to regulate that. Another example would be to increase transparency about accidents in BSL-4 facilities. They’re the highest level of biosecurity. Most people are unaware that there was a major outbreak that did serious economic damage in Britain that was caused from something coming out of a BSL-4 facility. That was the foot-and-mouth outbreak; it came out of a Pirbright facility.

Arden Koehler: And this was due to weak regulation or people not following the–

Toby Ord: It came out of a leaking pipe and it was first noticed in the field next to the facility that was working on exactly the same strain of foot-and-mouth. And they found the pipe, but it’s not widely known that it came from this government research because the government did not promote knowledge of that. And they renewed their license and two weeks later it leaked out again.

Arden Koehler: Wow.

Toby Ord: So, that seems pretty crazy to me. For people who say, “Don’t worry about this gain-of-function research, it’s in a BSL-3 enhanced facility”. The fact that there’s a BSL-4 facility that was so poorly run that they let them leak something out two weeks after they renewed their license.

Robert Wiblin: Yeah. This is something we need to happen zero times ever.

Toby Ord: Yeah.

Robert Wiblin: And it’s happened twice at the same place in a few weeks apart.

Toby Ord: So yeah. That’s how I see it, which is for certain things, such as taking some of the most dangerous diseases known to humanity, say smallpox research, particularly if you’re increasing its lethality or something. That it’s not enough to do this in BSL-3 or BSL-3 enhanced, and that it’s not even enough to do it in BSL-4. It should be in a level that has never had an escape, and where once it’s had an escape, you need to increase the level.

Robert Wiblin: Now it’s BSL-6!

Toby Ord: Yes. Something like that. The last death of smallpox in the world was in Britain where it leaked out of a lab. Less well known is that that lab, it had also escaped from it previously. So, there are a lot of people trying to do their best. And I’m sure a lot of labs, they really are doing really well. I don’t know whether these are problems of policy or problems of implementation. But whatever they are, there’s some kind of a problem.

Robert Wiblin: I mean, it is very hard in a big organization to never mess up. There’s so many ways to mess up.

Toby Ord: That’s right. Maybe we don’t yet deserve to be able to work on these things until we have worked out a way to not mess up or that’s at least a level beyond the current levels that we know that have messed up. So that’s an example of some policy recommendations.

Robert Wiblin: I just want to say it’s incredible that it is not mandatory to declare violations or ways in which a BSL-4 containment is breached. It’s incredible.

Toby Ord: Yeah. That’s right.

Robert Wiblin: That’s all I’ve got to say.

Toby Ord: So in another sense, it’s another obvious policy recommendation. But it’s only obvious once you find out that it’s not already implemented. So, I’ve tried to play it pretty safe on those. And then yeah, also have recommendations of what individuals should do.

Careers [03:04:54]
Robert Wiblin: Yeah, let’s talk about that. I guess, you haven’t spent years working on career choice, specifically. That’s meant to be our job. But do you have any recommendations for listeners? Maybe we could start with younger listeners. Perhaps people in their 20’s. Do you have any advice for how they can contribute?

Toby Ord: Yeah, so I think that if they’re in the biological sciences, then they may want to think seriously about working on risk from engineered pandemics. If they’re in computer science, or those kinds of areas, they might want to think seriously, let’s say mathematics, about working on aligning artificial general intelligence with human values. If they’re in philosophy, which is not that common, but quite common among the people who listen to this episode–

Robert Wiblin: There are dozens of us!

Toby Ord: I would suggest, actually, I think work on existential risk on the whole, the type of thing this book is trying to do is really neglected. I think there’s just a couple of people working on it full-time in the whole world, whereas at least AI alignment now has dozens and I think there’s probably a lot of issues about the ethics of this that could be explored. So yes, that’s research approaches. I think climate science, if someone’s doing earth sciences or atmospheric sciences, or they could imagine doing that, then working on extreme climate risks. I think in economics you could help with a lot of those areas, as well. And then also, if you’re in policy, you could try to get into a position where you could help with the policy on these types of issues. And it’s also obviously very important that the people in policy work with the people in academia from both sides. Both that the policy people get the skills and reach out, and also that the people in academia have an eye to policy and trying to relate to it.

Robert Wiblin: Yeah. We also have a lot of listeners who are between 30 and 70, I guess. Already well into their careers and there’s this one sense in which they’re in a much better position to make a difference because they have a lot more career capital and a lot more power, potentially. But then they feel more hemmed in by the constraints of their existing career. Do you have any advice for them? I guess those people who are in government as a particularly common case.

Toby Ord: Yeah. There’s a few things that people can do. If they’re in government, then I think that probably something that utilizes that fact is probably best. I think starting some of these conversations about how we should be thinking about these big picture questions about the future of humanity. Now, you might say that’s a little bit too much for government. If they’re in the treasury, they could maybe try to get discount rates lowered in their treasury handbooks. There’s some close connections there with economics and how we think about the long-term future. They could try to think about things to do with biosecurity or international diplomacy around that. There’s a couple of ideas there.

Toby Ord: But I think that having influential people start to open up this greater public conversation about how we should take these threats seriously. This can’t just be above everyone’s pay grade or just a thing that people say, “Well, it sounds really important but I guess I’m not going to talk about it because it seems a bit outlandish”. We need to make it seem a bit less outlandish by having sensible conversations about it coming from people whose views other people respect. So, if people respect your views, then you’re in a good position to talk about this stuff.

Robert Wiblin: And if they disrespect your views, I guess, close the book and–

Toby Ord: If people disrespect your views, then talking about it may be counterproductive.

Robert Wiblin: Yeah.

Arden Koehler: Yeah. Do you think there are symbolic actions that could be really valuable? You mentioned in the book that there’s this UNESCO declaration on the responsibilities of present generations toward future generations. That was in 1997. I didn’t know about that until I read it in the book, and maybe suggests that it didn’t have much of an effect, but do you feel that there are things like that that we could do that just declare that this is an important issue that might actually be helpful?

Toby Ord: Possibly. I think that it’s probably good that that declaration was made. It certainly seems to show, at one level, that you can have conversations about things like this within the UN. But at another level, that they don’t always do anything. This goes back to what you were saying before about, “Hey, maybe ethics can change to encompass these ideas as part of common sense morality”, but it may still not have much effect. So, there’s good news and there’s bad news. I think that various countries have explored having changes to their democratic process in order to represent future generations. A commonly thought of case is Wales, where there’s a commissioner for future generations. And there are other cases where they’ve made constitutional changes. But the commissioner for future generations in Wales doesn’t spend, I think, any of their time on thinking about these types of issues for risks facing humanity, and also they have no actual binding power. And there’s a bill in government in the UK at the moment, in parliament I should say, in the house of Lords, the Lord Bird’s bill, on the wellbeing of future generations. And it’s trying to implement this Welsh approach in the UK and enhance it in a few ways.

Toby Ord: I really applaud the sentiment of this. I am unsure, when it comes to political theory, as to whether something like this is getting a foot in the door and really the first step that will then help you really achieve a much more powerful representation of the future. Or whether it could be the thing that then feels like, “Oh, we’ve done that. We’ve got this commissioner for the future generations. Your critique now has been answered and the wind comes out of your sails”. I actually just don’t know which of those it is. So I don’t know if something is symbolic, I don’t know if it’s then just token.

Robert Wiblin: So we’ve talked about how people can contribute through their careers, but it’s not the only way that people try to make a difference. Are there any things you think people can do in their ordinary lives that can potentially help to reduce existential risks?

Toby Ord: Yeah. So I think that one major area is donations. There are plenty of people working to try to help with a lot of these issues and they’re not always fully funded. So, that’s a way which you can use your career, turn what you’re good at, into helping pay for time for other people to work on these things.

Toby Ord: And we sometimes think of that as maybe the existential risk organizations, in particular. Those who are focused on existential risk overall. It also includes ones who are focused on particular existential risks. And it also includes existential risk factors. And maybe that’s something that’s a bit neglected up until now. I don’t know who the best organization working to prevent great power war is, but I should find out. It sounds quite important. And so there may be some areas like this that actually could accept quite a bit more funding. And then another thing, more generally, is for people to have this public conversation. To try to just start talking about this stuff and to try and talk about it in a way that is powerful and that will catch on, rather than a way that feels really contrarian, I think.

Toby Ord: I think that’s been a bit of a mistake in the past. You get more interest initially if you say, “Hey, you thought saving people’s lives was the most important thing, actually working on computer programs…” Something like that that tries to sound contrarian, I think that the time for that has gone and that you’re better off trying to have something that sounds like something that is actually just naturally and deeply true in your argument. And talking about these things in your family and your workplace and, more broadly, if you think that you’re persuasive and able to actually help with that conversation.

Robert Wiblin: You’re reluctant to pitch yourself here, Toby, but you have this book, I’ve heard. So I guess most people could go out and buy that and potentially, if you know someone who’s influencing and someone else who could take action, perhaps even if you can’t, perhaps giving them this book is a decent place to begin.

Toby Ord: Yeah, I mean the book, “The Precipice”, is out in the UK on the 5th of March. In the US on the 24th March. It’s something that I’ve written for a lot of audiences simultaneously. So it’s two books in one or something that somehow, outrageously, my publishers let me include as many pages of endnotes and appendices as there are pages of the main text.

Toby Ord: So there’s this expanded book that’s twice as long. And I think that the people who already care about existential risk will want to do that. They will want to really dive into these endnotes. They’re not just citations. They’re really interesting side stories and anecdotes and so on that were perhaps more interesting than some of the text in the book, but would take me too far off course. And so they can get into those kinds of areas. Whereas, I’ve kept the main text of the book to the central arguments to get through this and to be extremely readable. So, I think it’s the kind of thing that people who haven’t heard about this issue: send a copy to your parents. That would work. If there’s people in your life that you’ve always wanted to get to care about this and it’s never quite worked out, then I think this is a good use of this, as well as for people who are in, say, the effective altruism community that have always been a bit suspicious about this existential risk thing. I think that I’m trying to make a case here which hopefully appeals and talks to you.

Robert Wiblin: Well, we’ve run out of time. We managed to get through about three quarters of the questions, but I suppose that’s just the beginning of the list for a new interview in two years time. We can go back and find out what we didn’t manage to get to today.

Toby Ord: Yeah. We’ll have to schedule six hours for that one.

Robert Wiblin: Yeah. I wonder what the longest interview will be by then. All right. My guest today has been Toby Ord and my co host has been Arden Koehler. Thanks so much for coming on the show, guys.

Toby Ord: Yeah, great to be here.

Arden Koehler: This was really fun.'''

blog_post = re.split('Robert Wilbin:|Toby Ord:|Arden Koehler:', blog_post)



trainer = ListTrainer(chatbot)

#trainer.train(blog_post)

response = chatbot.get_response('How are you doing today?')

print(response)