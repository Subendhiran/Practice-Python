import os

def open_edge_tabs(num_tabs):
    url = "https://www.google.com"
    for i in range(num_tabs):
        os.system(f"start msedge {url}")


open_edge_tabs(10)