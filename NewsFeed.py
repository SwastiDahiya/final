from tkinter import *
from data_handler import DataHandler
from functools import partial
from PIL import ImageTk, Image

class Home(Frame):
    def __init__(self,master):
        super().__init__(master)

        #Image load..
        self.img = ImageTk.PhotoImage(Image.open('news.png'))
        self.i = Label(self,image = self.img,bg = 'orange',width = 850)
        self.i.grid(row = 1,columnspan = 9)

        #File load..
        self.data_handler = DataHandler("data.json")
        self.category_lists = self.data_handler.get_categories_list()
        self.category_data_labels = []

        #add button on screen for each category..
        self.b1 = Button(self,font = ('Times New Roman',10),bg = 'pink',width = 12,text = self.category_lists[0],command = self.b1)
        self.b2 = Button(self,font = ('Times New Roman',10),bg = 'pink',width = 12,text = self.category_lists[1],command = self.b2)
        self.b3 = Button(self,font = ('Times New Roman',10),bg = 'pink',width = 12,text = self.category_lists[2],command = self.b3)
        self.b4 = Button(self,font = ('Times New Roman',10),bg = 'pink',width = 12,text = self.category_lists[3],command = self.b4)
        self.b5 = Button(self,font = ('Times New Roman',10),bg = 'pink',width = 12,text = self.category_lists[4],command = self.b5)
        self.b6 = Button(self,font = ('Times New Roman',10),bg = 'pink',width = 12,text = self.category_lists[5],command = self.b6)
        self.b7 = Button(self,font = ('Times New Roman',10),bg = 'pink',width = 12,text = self.category_lists[6],command = self.b7)
        self.b8 = Button(self,font = ('Times New Roman',10),bg = 'pink',width = 12,text = self.category_lists[7],command = self.b8)
        self.b9 = Button(self,font = ('Times New Roman',10),bg = 'pink',width = 12,text = self.category_lists[8],command = self.b9)

        #griding of all Buttons..
        self.b1.grid(row = 0,column = 0)
        self.b2.grid(row = 0,column = 1)
        self.b3.grid(row = 0,column = 2)
        self.b4.grid(row = 0,column = 3)
        self.b5.grid(row = 0,column = 4)
        self.b6.grid(row = 0,column = 5)
        self.b7.grid(row = 0,column = 6)
        self.b8.grid(row = 0,column = 7)
        self.b9.grid(row = 0,column = 8)

        self.pack()

    def b1(self):
        root = Tk()
        obj = Headlines(root)
        root.title('Headlines')
        root.mainloop()
    
    def b2(self):
        root = Tk()
        obj = Entertainment(root)
        root.title('Entertainment')
        root.mainloop()
    
    def b3(self):
        root = Tk()
        obj = Politics(root)
        root.title('Politics')
        root.mainloop()
    
    def b4(self):
        root = Tk()
        obj = Health(root)
        root.title('Health')
        root.mainloop()
    
    def b5(self):
        root = Tk()
        obj = Business(root)
        root.title('Business')
        root.mainloop()
    
    def b6(self):
        root = Tk()
        obj = Science(root)
        root.title('Science')
        root.mainloop()
    
    def b7(self):
        root = Tk()
        obj = Technology(root)
        root.title('Technology')
        root.mainloop()
    
    def b8(self):
        root = Tk()
        obj = Education(root)
        root.title('Education')
        root.mainloop()
    
    def b9(self):
        root = Tk()
        obj = Sports(root)
        root.title('Sports')
        root.mainloop()

class Headlines(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.data_handler = DataHandler("data.json")
        self.category_lists = self.data_handler.get_categories_list()
        self.category_data_labels = []

        self.element = 'Headlines'
        
        #delete old labels..
        for self.element in self.category_data_labels:
            self.element.configure(text = "")
            del self.element

        #add new labels for name..
        self.list_data_for_category = self.data_handler.get_news_for_category(self.element)
        for i in range(len(self.list_data_for_category)):
            self.element = self.list_data_for_category[i]
            self.labelfont = ('times',15,'bold')
            self.labelcontent_font = ('times',10,'bold','italic')
            self.label_heading = Label(self, text = self.element['headline'])
            self.label_heading.config(font = self.labelfont)
            self.label_heading.grid(column = 0, row = 3*i)
            self.label_content = Label(self, text = self.element['content'])
            self.label_content.config(font = self.labelcontent_font)
            self.label_content.grid(column = 0, row = 3*i+1)
            self.label_content_separator = Label(self, text = '---------------------------')
            self.label_content_separator.grid(column = 0, row=3*i+2)
            self.category_data_labels.append(self.label_heading)
            self.category_data_labels.append(self.label_content)
            self.category_data_labels.append(self.label_content_separator)

        self.pack()

class Entertainment(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.data_handler = DataHandler("data.json")
        self.category_lists = self.data_handler.get_categories_list()
        self.category_data_labels = []

        self.element = 'Entertainment'
        
        #delete old labels..
        for self.element in self.category_data_labels:
            self.element.configure(text = "")
            del self.element

        #add new labels for name..
        self.list_data_for_category = self.data_handler.get_news_for_category(self.element)
        for i in range(len(self.list_data_for_category)):
            self.element = self.list_data_for_category[i]
            self.labelfont = ('times',15,'bold')
            self.labelcontent_font = ('times',10,'bold','italic')
            self.label_heading = Label(self, text = self.element['headline'])
            self.label_heading.config(font = self.labelfont)
            self.label_heading.grid(column = 0, row = 3*i)
            self.label_content = Label(self, text = self.element['content'])
            self.label_content.config(font = self.labelcontent_font)
            self.label_content.grid(column = 0, row = 3*i+1)
            self.label_content_separator = Label(self, text = '---------------------------')
            self.label_content_separator.grid(column = 0, row=3*i+2)
            self.category_data_labels.append(self.label_heading)
            self.category_data_labels.append(self.label_content)
            self.category_data_labels.append(self.label_content_separator)

        self.pack()

class Politics(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.data_handler = DataHandler("data.json")
        self.category_lists = self.data_handler.get_categories_list()
        self.category_data_labels = []

        self.element = 'Politics'
        
        #delete old labels..
        for self.element in self.category_data_labels:
            self.element.configure(text = "")
            del self.element

        #add new labels for name..
        self.list_data_for_category = self.data_handler.get_news_for_category(self.element)
        for i in range(len(self.list_data_for_category)):
            self.element = self.list_data_for_category[i]
            self.labelfont = ('times',15,'bold')
            self.labelcontent_font = ('times',10,'bold','italic')
            self.label_heading = Label(self, text = self.element['headline'])
            self.label_heading.config(font = self.labelfont)
            self.label_heading.grid(column = 0, row = 3*i)
            self.label_content = Label(self, text = self.element['content'])
            self.label_content.config(font = self.labelcontent_font)
            self.label_content.grid(column = 0, row = 3*i+1)
            self.label_content_separator = Label(self, text = '---------------------------')
            self.label_content_separator.grid(column = 0, row=3*i+2)
            self.category_data_labels.append(self.label_heading)
            self.category_data_labels.append(self.label_content)
            self.category_data_labels.append(self.label_content_separator)

        self.pack()

class Health(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.data_handler = DataHandler("data.json")
        self.category_lists = self.data_handler.get_categories_list()
        self.category_data_labels = []

        self.element = 'Health'
        
        #delete old labels..
        for self.element in self.category_data_labels:
            self.element.configure(text = "")
            del self.element

        #add new labels for name..
        self.list_data_for_category = self.data_handler.get_news_for_category(self.element)
        for i in range(len(self.list_data_for_category)):
            self.element = self.list_data_for_category[i]
            self.labelfont = ('times',15,'bold')
            self.labelcontent_font = ('times',10,'bold','italic')
            self.label_heading = Label(self, text = self.element['headline'])
            self.label_heading.config(font = self.labelfont)
            self.label_heading.grid(column = 0, row = 3*i)
            self.label_content = Label(self, text = self.element['content'])
            self.label_content.config(font = self.labelcontent_font)
            self.label_content.grid(column = 0, row = 3*i+1)
            self.label_content_separator = Label(self, text = '---------------------------')
            self.label_content_separator.grid(column = 0, row=3*i+2)
            self.category_data_labels.append(self.label_heading)
            self.category_data_labels.append(self.label_content)
            self.category_data_labels.append(self.label_content_separator)

        self.pack()

class Business(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.data_handler = DataHandler("data.json")
        self.category_lists = self.data_handler.get_categories_list()
        self.category_data_labels = []

        self.element = 'Business'
        
        #delete old labels..
        for self.element in self.category_data_labels:
            self.element.configure(text = "")
            del self.element

        #add new labels for name..
        self.list_data_for_category = self.data_handler.get_news_for_category(self.element)
        for i in range(len(self.list_data_for_category)):
            self.element = self.list_data_for_category[i]
            self.labelfont = ('times',15,'bold')
            self.labelcontent_font = ('times',10,'bold','italic')
            self.label_heading = Label(self, text = self.element['headline'])
            self.label_heading.config(font = self.labelfont)
            self.label_heading.grid(column = 0, row = 3*i)
            self.label_content = Label(self, text = self.element['content'])
            self.label_content.config(font = self.labelcontent_font)
            self.label_content.grid(column = 0, row = 3*i+1)
            self.label_content_separator = Label(self, text = '---------------------------')
            self.label_content_separator.grid(column = 0, row=3*i+2)
            self.category_data_labels.append(self.label_heading)
            self.category_data_labels.append(self.label_content)
            self.category_data_labels.append(self.label_content_separator)

        self.pack()

class Science(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.data_handler = DataHandler("data.json")
        self.category_lists = self.data_handler.get_categories_list()
        self.category_data_labels = []

        self.element = 'Science'
        
        #delete old labels..
        for self.element in self.category_data_labels:
            self.element.configure(text = "")
            del self.element

        #add new labels for name..
        self.list_data_for_category = self.data_handler.get_news_for_category(self.element)
        for i in range(len(self.list_data_for_category)):
            self.element = self.list_data_for_category[i]
            self.labelfont = ('times',15,'bold')
            self.labelcontent_font = ('times',10,'bold','italic')
            self.label_heading = Label(self, text = self.element['headline'])
            self.label_heading.config(font = self.labelfont)
            self.label_heading.grid(column = 0, row = 3*i)
            self.label_content = Label(self, text = self.element['content'])
            self.label_content.config(font = self.labelcontent_font)
            self.label_content.grid(column = 0, row = 3*i+1)
            self.label_content_separator = Label(self, text = '---------------------------')
            self.label_content_separator.grid(column = 0, row=3*i+2)
            self.category_data_labels.append(self.label_heading)
            self.category_data_labels.append(self.label_content)
            self.category_data_labels.append(self.label_content_separator)

        self.pack()

class Technology(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.data_handler = DataHandler("data.json")
        self.category_lists = self.data_handler.get_categories_list()
        self.category_data_labels = []

        self.element = 'Technology'
        
        #delete old labels..
        for self.element in self.category_data_labels:
            self.element.configure(text = "")
            del self.element

        #add new labels for name..
        self.list_data_for_category = self.data_handler.get_news_for_category(self.element)
        for i in range(len(self.list_data_for_category)):
            self.element = self.list_data_for_category[i]
            self.labelfont = ('times',15,'bold')
            self.labelcontent_font = ('times',10,'bold','italic')
            self.label_heading = Label(self, text = self.element['headline'])
            self.label_heading.config(font = self.labelfont)
            self.label_heading.grid(column = 0, row = 3*i)
            self.label_content = Label(self, text = self.element['content'])
            self.label_content.config(font = self.labelcontent_font)
            self.label_content.grid(column = 0, row = 3*i+1)
            self.label_content_separator = Label(self, text = '---------------------------')
            self.label_content_separator.grid(column = 0, row=3*i+2)
            self.category_data_labels.append(self.label_heading)
            self.category_data_labels.append(self.label_content)
            self.category_data_labels.append(self.label_content_separator)

        self.pack()

class Education(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.data_handler = DataHandler("data.json")
        self.category_lists = self.data_handler.get_categories_list()
        self.category_data_labels = []

        self.element = 'Headlines'
        
        #delete old labels..
        for self.element in self.category_data_labels:
            self.element.configure(text = "")
            del self.element

        #add new labels for name..
        self.list_data_for_category = self.data_handler.get_news_for_category(self.element)
        for i in range(len(self.list_data_for_category)):
            self.element = self.list_data_for_category[i]
            self.labelfont = ('times',15,'bold')
            self.labelcontent_font = ('times',10,'bold','italic')
            self.label_heading = Label(self, text = self.element['headline'])
            self.label_heading.config(font = self.labelfont)
            self.label_heading.grid(column = 0, row = 3*i)
            self.label_content = Label(self, text = self.element['content'])
            self.label_content.config(font = self.labelcontent_font)
            self.label_content.grid(column = 0, row = 3*i+1)
            self.label_content_separator = Label(self, text = '---------------------------')
            self.label_content_separator.grid(column = 0, row=3*i+2)
            self.category_data_labels.append(self.label_heading)
            self.category_data_labels.append(self.label_content)
            self.category_data_labels.append(self.label_content_separator)

        self.pack()

class Sports(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.data_handler = DataHandler("data.json")
        self.category_lists = self.data_handler.get_categories_list()
        self.category_data_labels = []

        self.element = 'Sports'
        
        #delete old labels..
        for self.element in self.category_data_labels:
            self.element.configure(text = "")
            del self.element

        #add new labels for name..
        self.list_data_for_category = self.data_handler.get_news_for_category(self.element)
        for i in range(len(self.list_data_for_category)):
            self.element = self.list_data_for_category[i]
            self.labelfont = ('times',15,'bold')
            self.labelcontent_font = ('times',10,'bold','italic')
            self.label_heading = Label(self, text = self.element['headline'])
            self.label_heading.config(font = self.labelfont)
            self.label_heading.grid(column = 0, row = 3*i)
            self.label_content = Label(self, text = self.element['content'])
            self.label_content.config(font = self.labelcontent_font)
            self.label_content.grid(column = 0, row = 3*i+1)
            self.label_content_separator = Label(self, text = '---------------------------')
            self.label_content_separator.grid(column = 0, row=3*i+2)
            self.category_data_labels.append(self.label_heading)
            self.category_data_labels.append(self.label_content)
            self.category_data_labels.append(self.label_content_separator)

        self.pack()
        
root = Tk()
obj = Home(root)
root.configure(bg = 'orange')
root.title('NewsFeed')
root.mainloop()
