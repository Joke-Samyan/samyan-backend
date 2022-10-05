import motor.motor_asyncio
from pymongo import MongoClient
import bson



def insert_dataset(dataset_data):
    try:
        dataset_data["entries_count"] = len(dataset_data["entries"])
        dataset_collection.insert_one(dataset_data)
        return True
    except Exception as e:
        print(e)
        return False

def find_dataset_by_id(id):
    result = dataset_collection.find_one({"_id": bson.ObjectId(id)})
    print(result)
    data = {}
    for i in result:
        data[i] = result[i]
    return data
    # return result
# print(retrieve_datasets())
# print(insert_dataset(dataset_data))
# print(find_dataset_by_id("631787cdf0dab8c522bdf91a"))

# async def insert_dataset(dataset_data):
#     dataset = await dataset_collection.insert_one(dataset_data)
#     new_dataset = await dataset_collection.find_one({"_id": dataset.inserted_id})
#     return True

# async def retrieve_datasets():
#     return [dataset async for dataset in dataset_collection.find()]

# async def find_dataset_by_id(id):
#     dataset = await dataset_collection.find_one({"_id" : id})
#     if dataset:
#         return dataset["owner"]
#     else:
#         return None