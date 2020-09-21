from gtts import gTTS

l = "শ্রী তারাশঙ্কর বন্দ্যোপাধ্যায় গাড়ি কিনেছেন।বন্ধু সাহিত্যিক শ্রী বিভুতিভূষন বন্দ্যোপাধ্যায় চতুর্দিকে ঢাক পিটিয়ে তা বলে বেড়াচ্ছেন।একজন বললেন -উনি গাড়ি কিনেছেন তাতে আপনার কি?"

def bangla(tex,filename):
    lan="bn"
    d = gTTS(text=tex, lang=lan, slow=False)
    d.save(filename)

bangla(l,"banga.mp3")

