def generate_document(data):
    lang = data["language"]
    dt = data["document_type"]

    if lang == "Tamil":
        return tamil_template(data, dt)
    if lang == "Hindi":
        return hindi_template(data, dt)
    return english_template(data, dt)

def english_template(d, dt):
    return f"""DRAFT LEGAL DOCUMENT
{dt.upper()}

Date: {d['date']}

FIRST PARTY / APPLICANT:
{d['party_a']}

SECOND PARTY / RESPONDENT:
{d['party_b'] or '[TO BE FILLED]'}

ADDRESS:
{d['address'] or '[TO BE FILLED]'}

PURPOSE:
{d['purpose']}

DURATION:
{d['duration'] or '[TO BE FILLED]'}

AMOUNT / CONSIDERATION:
{d['amount'] or '[TO BE FILLED]'}

TERMS:
{d['extra'] or '[TO BE FILLED]'}

DECLARATION
The parties state that the information provided for this draft is accurate to the best of their knowledge and that they intend to comply with the applicable terms and laws.

SIGNATURES

First Party / Applicant: ______________________

Second Party / Respondent: ____________________

Date: ____________________

IMPORTANT REVIEW NOTICE
This is an AI-assisted educational draft, not legal advice. The document should be checked and adapted by a qualified legal professional before signing, filing, or relying on it.
"""

def tamil_template(d, dt):
    return f"""வரைவு சட்ட ஆவணம்
{dt}

தேதி: {d['date']}

முதல் தரப்பு / விண்ணப்பதாரர்:
{d['party_a']}

இரண்டாம் தரப்பு / எதிர் தரப்பு:
{d['party_b'] or '[நிரப்ப வேண்டியது]'}

முகவரி:
{d['address'] or '[நிரப்ப வேண்டியது]'}

நோக்கம்:
{d['purpose']}

காலம்:
{d['duration'] or '[நிரப்ப வேண்டியது]'}

தொகை / பரிசீலனைத் தொகை:
{d['amount'] or '[நிரப்ப வேண்டியது]'}

கூடுதல் விதிமுறைகள்:
{d['extra'] or '[நிரப்ப வேண்டியது]'}

உறுதிமொழி
மேலே வழங்கப்பட்ட தகவல்கள் தங்களது அறிவிற்கு எட்டிய வரையில் சரியானவை என்று தரப்பினர் உறுதிப்படுத்துகின்றனர்.

கையொப்பங்கள்

முதல் தரப்பு / விண்ணப்பதாரர்: ______________________

இரண்டாம் தரப்பு / எதிர் தரப்பு: ______________________

தேதி: ____________________

முக்கிய அறிவிப்பு:
இது கல்வி நோக்கத்திற்கான AI உதவியுடன் உருவாக்கப்பட்ட வரைவு மட்டுமே. கையொப்பமிடுவதற்கு அல்லது சட்டரீதியாக பயன்படுத்துவதற்கு முன் தகுதியான சட்ட நிபுணரால் சரிபார்க்கப்பட வேண்டும்.
"""

def hindi_template(d, dt):
    return f"""कानूनी दस्तावेज़ का प्रारूप
{dt}

दिनांक: {d['date']}

प्रथम पक्ष / आवेदक:
{d['party_a']}

द्वितीय पक्ष / प्रतिवादी:
{d['party_b'] or '[भरना बाकी]'}

पता:
{d['address'] or '[भरना बाकी]'}

उद्देश्य:
{d['purpose']}

अवधि:
{d['duration'] or '[भरना बाकी]'}

राशि / प्रतिफल:
{d['amount'] or '[भरना बाकी]'}

अतिरिक्त शर्तें:
{d['extra'] or '[भरना बाकी]'}

घोषणा
पक्षकार पुष्टि करते हैं कि उपलब्ध कराई गई जानकारी उनकी जानकारी के अनुसार सही है।

हस्ताक्षर

प्रथम पक्ष / आवेदक: ______________________

द्वितीय पक्ष / प्रतिवादी: __________________

दिनांक: ____________________

महत्वपूर्ण सूचना:
यह केवल शैक्षिक उद्देश्य के लिए AI-सहायित प्रारूप है। हस्ताक्षर या वास्तविक कानूनी उपयोग से पहले योग्य कानूनी पेशेवर से इसकी समीक्षा कराएं।
"""
