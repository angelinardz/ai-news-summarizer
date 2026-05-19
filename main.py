import tkinter as tk
from logic import get_news_data

#functions
"""Updates the given widget with the provided text, 
making it editable temporarily to allow for updates, 
then sets it back to disabled with a specific background and text color."""

def update(widget,text):
    widget.config(state='normal')
    widget.delete('1.0',"end")
    widget.insert('1.0',text)
    widget.config(state='disabled',bg='#f0f0f0',fg='black')

"""Fetches news data from the URL provided in the urlText widget,"""
def summarizeNewsUrl():
    
    url=urlText.get('1.0',"end-1c").strip()
    
    if not url:
        return 
    
    try:
        data = get_news_data(url)
        update(title, data["title"])
        update(authors,data["authors"])
        update(date, data["publish_date"])
        update(summary, data["summary"])
        update(sentimentAnalysis, data["sentiment"])
    
    except Exception as e:
        update(sentimentAnalysis, f"Error fetching article: {e}")

    


root=tk.Tk()
root.title("News Article Summarizer")
root.geometry("1200x600")


tlabel=tk.Label(root,text="Title")
tlabel.pack()

title=tk.Text(root,height=1,width=140) 
title.config(state='disabled')
title.pack()

alabel=tk.Label(root,text="Author")
alabel.pack()

authors=tk.Text(root,height=1,width=140) 
authors.config(state='disabled')
authors.pack()

plabel=tk.Label(root,text="Publication Date")
plabel.pack()

date=tk.Text(root,height=1,width=140) 
date.config(state='disabled')
date.pack()


slabel=tk.Label(root,text="Summary")
slabel.pack()

summary=tk.Text(root,height=20,width=140) 
summary.config(state='disabled')
summary.pack()

selabel=tk.Label(root,text="Sentiment Analysis")
selabel.pack()

sentimentAnalysis=tk.Text(root,height=1,width=140) 
sentimentAnalysis.config(state='disabled')
sentimentAnalysis.pack()

ulabel=tk.Label(root,text="URL")
ulabel.pack()

urlText=tk.Text(root,height=1,width=140)
urlText.pack() 

btn=tk.Button(root,text="Summarize",command=summarizeNewsUrl)
btn.pack()



root.mainloop()


