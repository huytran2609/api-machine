# import json
# import pickle
# from scipy.spatial import KDTree
# from sentence_transformers import SentenceTransformer
# from pathlib import Path

# """
# Using:
# - SentenceTransformer
# - KDTree (scipy)
# """
# # specifying the SentenceTransformer model
# model_name = "all-mpnet-base-v2"  # Dimensions: 768


# def init_chatbot():
#     # specifying data
#     path = Path(__file__).parent.absolute()
#     answer_file = f"{path}/answers.bin"
#     kdtree_file = f"{path}/kdtree.bin"
#     # loading data
#     model = SentenceTransformer(model_name)
#     with open(kdtree_file, "rb") as infile:
#         kdtree: KDTree = pickle.load(infile)
#     with open(answer_file, "rb") as infile:
#         answers = pickle.load(infile)
#     return model, kdtree, answers


# def chatbot(model, kdtree, answers, question):
#     if question == "":
#         messages = "Bạn còn câu hỏi nào khác không?"
#         return json.dumps({"messages": messages}, ensure_ascii=False).encode("utf-8")
#     try:
#         # convert the question to vector
#         vector = model.encode(question)
#         # executing the KD-Tree(vector,5)
#         _, idxes = kdtree.query(vector, k=5)
#         # get the answer
#         answer = answers[idxes[0]]
#         return answer
#     except IndexError:
#         answer = "Xin lỗi! Chúng tôi chưa hiểu câu hỏi của bạn"
#         return answer
