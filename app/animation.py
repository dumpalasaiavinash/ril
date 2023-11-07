def animation(playspeed,uniquekey):
    import json 
    import streamlit as st 
    from streamlit_lottie import st_lottie
    
    path = "talking_animation.json"
    with open(path,"r") as file: 
        talking_animation = json.load(file) 
   
        
    st_lottie(talking_animation, 
        reverse=True, 
        height=400, 
        width=400, 
        speed=playspeed, 
        loop=True, 
        quality='high', 
        key=uniquekey
    )
    return(uniquekey)


# def animation(playspeed,uniquekey):
#     import json 
#     import streamlit as st 
#     from streamlit_lottie import st_lottie 
#     import requests
    
#     # path = "talking_animation.json"
#     # with open(path,"r") as file: 
#     #     talking_animation = json.load(file) 
#     url = requests.get("https://lottie.host/642dc511-2170-498f-bead-6e6967798ecc/rgC18eaO77.json") 
#     url_json = dict() 
#     if url.status_code == 200: 
#         url_json = url.json() 
#     else: 
#         print("Error in URL") 
    
    
   
        
#     st_lottie(url_json, 
#         reverse=True, 
#         height=400, 
#         width=400, 
#         speed=playspeed, 
#         loop=True, 
#         quality='high', 
#         key=str(uniquekey)
#     )