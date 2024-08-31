import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Make sure to install pillow with 'pip install pillow'

class ScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scraper Application")
        self.root.geometry("500x400")

        # Create a frame for the main content
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create and pack the options label and checkboxes
        self.option_label = ttk.Label(self.main_frame, text="Choose scraping options:")
        self.option_label.pack(pady=10)

        self.var_phone = tk.BooleanVar()
        self.var_location = tk.BooleanVar()
        self.var_website = tk.BooleanVar()
        self.var_email = tk.BooleanVar()

        self.check_phone = ttk.Checkbutton(self.main_frame, text="Phone Number", variable=self.var_phone)
        self.check_location = ttk.Checkbutton(self.main_frame, text="Location", variable=self.var_location)
        self.check_website = ttk.Checkbutton(self.main_frame, text="Website", variable=self.var_website)
        self.check_email = ttk.Checkbutton(self.main_frame, text="Email", variable=self.var_email)

        self.check_phone.pack()
        self.check_location.pack()
        self.check_website.pack()
        self.check_email.pack()

        self.scrape_button = ttk.Button(self.main_frame, text="Scrape", command=self.show_input_page)
        self.scrape_button.pack(pady=10)

        self.result_label = ttk.Label(self.main_frame, text="")
        self.result_label.pack(pady=10)

    def show_input_page(self):
        # Hide the main content
        self.main_frame.pack_forget()

        # Create a new frame for input
        self.input_frame = ttk.Frame(self.root, padding="10")
        self.input_frame.pack(fill=tk.BOTH, expand=True)

        # Create and pack the input label and entry
        self.page_label = ttk.Label(self.input_frame, text="Enter the page number to scrape:")
        self.page_label.pack(pady=10)

        self.page_entry = ttk.Entry(self.input_frame)
        self.page_entry.pack(pady=10)

        self.submit_button = ttk.Button(self.input_frame, text="Scrape", command=self.start_scraping)
        self.submit_button.pack(pady=10)

        self.back_button = ttk.Button(self.input_frame, text="Back", command=self.show_main_page)
        self.back_button.pack(pady=10)

    def show_main_page(self):
        # Hide the input frame
        self.input_frame.pack_forget()

        # Show the main content
        self.main_frame.pack(fill=tk.BOTH, expand=True)

    def start_scraping(self):
        page_number = self.page_entry.get()
        options = []
        if self.var_phone.get():
            options.append("Phone Number")
        if self.var_location.get():
            options.append("Location")
        if self.var_website.get():
            options.append("Website")
        if self.var_email.get():
            options.append("Email")

        if not options:
            self.result_label.config(text="Please select at least one option.")
            return

        if not page_number:
            self.result_label.config(text="Please enter a page number.")
            return

        # Hide the input page and show loading
        self.input_frame.pack_forget()
        self.loading_frame = ttk.Frame(self.root, padding="10")
        self.loading_frame.pack(fill=tk.BOTH, expand=True)

        self.loading_label = ttk.Label(self.loading_frame, text="Scraping in progress...")
        self.loading_label.pack(pady=10)

        self.progress = ttk.Progressbar(self.loading_frame, mode='indeterminate')
        self.progress.pack(pady=10, fill=tk.X)
        self.progress.start()

        # Start scraping simulation
        self.root.after(1000, self.simulate_scraping, page_number, options)

    def simulate_scraping(self, page_number, options):
        # Simulate scraping with a delay
        self.root.after(2000, self.finish_scraping, page_number, options)

    def finish_scraping(self, page_number, options):
        # Stop the progress bar and hide loading frame
        self.progress.stop()
        self.loading_frame.pack_forget()

        # Show results and GIF
        self.result_frame = ttk.Frame(self.root, padding="10")
        self.result_frame.pack(fill=tk.BOTH, expand=True)

        # Load and display GIF
        gif_path = 'success.gif'  # Path to your GIF file
        self.gif_image = Image.open(gif_path)
        self.gif_frames = [ImageTk.PhotoImage(self.gif_image.copy().convert('RGBA'))]
        try:
            while True:
                self.gif_image.seek(self.gif_image.tell() + 1)
                self.gif_frames.append(ImageTk.PhotoImage(self.gif_image.copy().convert('RGBA')))
        except EOFError:
            pass  # End of GIF frames

        self.gif_label = tk.Label(self.result_frame, image=self.gif_frames[0])
        self.gif_label.pack(pady=10)

        self.success_label = ttk.Label(self.result_frame, text=f"Data successfully saved to data.xlsx")
        self.success_label.pack(pady=10)

        # Update GIF animation
        self.animate_gif(0)

    def animate_gif(self, frame_index):
        if self.gif_frames:
            self.gif_label.config(image=self.gif_frames[frame_index])
            self.root.after(100, self.animate_gif, (frame_index + 1) % len(self.gif_frames))

# Create the Tkinter application
root = tk.Tk()
app = ScraperApp(root)
root.mainloop()









import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
url = 'https://www.google.com/localservices/prolist?g2lbs=AOHF13lk24s1DeHCnI7w0RcTTxlx_7ZF2zYvP8ilyd_Rko8Hr0K6qwZBayYUSFkqsbcLlwRDgkTyp8gyO3kH8fDSIJaKj6BIw_QW0MvuaK1pyhJSSFM6Seg%3D&hl=ru-UZ&gl=uz&cs=1&ssta=1&oq=Construction%20Companies%20In%20St.%20Lucia&src=2&sa=X&q=camera%20sales%20compaines%20in%20new%20york&ved=0CAUQjdcJahgKEwi49NWk9p-IAxUAAAAAHQAAAAAQmgM&scp=CgpnY2lkOnN0b3JlEgAaACoO0JzQsNCz0LDQt9C40L0%3D&slp=MgBAAVIECAIgAIgBAJoBBgoCFxkQAA%3D%3D'



response = requests.get(url)
data = []

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract company names
    company_name_tags = soup.find_all('div', class_='rgnuSb xYjf2e')
    company_names = [tag.text.strip() for tag in company_name_tags]

    # Extract other details
    div_tags = soup.find_all('div', class_='fQqZ2e')

    for div_tag in div_tags:
        # Initialize a dictionary to store the extracted data
        extracted_data = {
            "Company Name": None,
            "Website": None,
            "Phone": None,
            "Location": None
        }

        # Extract the website
        website_tag = div_tag.find('a', attrs={'aria-label': 'Сайт'})
        if website_tag:
            extracted_data["Website"] = website_tag.get('href')

        # Extract the phone number
        phone_tag = div_tag.find('a', attrs={'aria-label': 'Позвонить'})
        if phone_tag:
            extracted_data["Phone"] = phone_tag.get('data-phone-number')

        # Extract the location
        location_tag = div_tag.find('a', attrs={'aria-label': 'Маршрут'})
        if location_tag:
            extracted_data["Location"] = location_tag.get('href')

        # Assign a company name to each entry (assuming one-to-one mapping)
        if company_names:
            extracted_data["Company Name"] = company_names.pop(0)

        # Add the data to the list
        data.append(extracted_data)

# Create a DataFrame and save it to an Excel file
df = pd.DataFrame(data)
df.to_excel('data.xlsx', index=False)


