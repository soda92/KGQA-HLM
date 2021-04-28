# %%
from neo_db.query_graph import get_KGQA_answer
from KGQA.ltp_array import get_target_array, cut_words

# %%
seg, pos = cut_words("贾宝玉的爸爸的儿子的父亲")

# %%
arr = []
for k in zip(seg[0], pos[0]):
    if k[1] in ('nh', 'n'):
        arr.append(k[0])
print(arr)
# %%
question = "贾宝玉的爸爸的儿子的父亲"
json_data = get_KGQA_answer(get_target_array(str(question)))
print(json_data)
