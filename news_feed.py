import tkinter
from data_handler import DataHandler
from functools import partial
from PIL import ImageTk, Image

window = tkinter.Tk()
window.title("News")
window.geometry('1000x600')

category_list_frame = tkinter.Frame(window)
category_list_frame.pack(side=tkinter.TOP, fill=tkinter.X)


content_frame = tkinter.Frame(window,bg='red')
content_frame.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)

vertical_scroll_bar = tkinter.Scrollbar(content_frame)
vertical_scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

data_container_canvas = tkinter.Canvas(content_frame,bg='orange',yscrollcommand=vertical_scroll_bar.set)
data_container_canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
img = ImageTk.PhotoImage(Image.open('news.jpg'))

app_image = data_container_canvas.create_image((50,10),image=img, anchor=tkinter.NW)

vertical_scroll_bar.configure(command=data_container_canvas.yview)

data_container_frame = tkinter.Frame(data_container_canvas)

data_container_canvas.create_window((4,4), window=data_container_frame, anchor=tkinter.NW)

def onFrameConfigure(event):
    '''Reset the scroll region to encompass the inner frame'''
    data_container_canvas.configure(scrollregion=data_container_canvas.bbox(tkinter.ALL))

def get_data_for_category(name):
    return data_handler.get_news_for_category(name)

def open_category(name):
    print(name)
    data_container_frame.config(height=600,width=950)
    # delete old labels
    for element in category_data_labels:
        element.configure(text="")
        del element
    # add new lables for name
    list_data_for_category = get_data_for_category(name)
    for i in range(len(list_data_for_category)):
        element = list_data_for_category[i]
        labelfont=('times',15,'bold')
        labelcontent_font=('times',10,'bold','italic')
        label_heading = tkinter.Label(data_container_frame, text=element['headline'])
        label_heading.config(font=labelfont)
        label_heading.grid(column=0, row=3*i)
        label_content = tkinter.Label(data_container_frame, text=element['content'])
        label_content.config(font=labelcontent_font)
        label_content.grid(column=0, row=3*i+1)
        label_content_separator = tkinter.Label(data_container_frame, text='---------------------------')
        label_content_separator.grid(column=0, row=3*i+2)
        category_data_labels.append(label_heading)
        category_data_labels.append(label_content)
        category_data_labels.append(label_content_separator)

data_handler = DataHandler("data.json")
category_lists = data_handler.get_categories_list()
category_data_labels = []

# add button on screen for each category
for i in range(len(category_lists)):
	element = category_lists[i]
	command_func = partial(open_category, element)
	button = tkinter.Button(category_list_frame,font = ('Times New Roman',10),bg = 'steel blue',text=element, command=command_func)
	button.grid(row=0, column=i)
#tkinter.Button(category_list_frame,font = ('Times New Roman',10),bg = 'steel blue',text=element, command=home)
#button.grid(row = 0,column = i)
data_container_frame.bind("<Configure>", onFrameConfigure)

window.mainloop()
