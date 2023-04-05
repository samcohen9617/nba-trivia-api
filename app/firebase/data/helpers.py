from firebase_admin import db


def get_data_from_firebase(collection):
    ref = db.reference(collection)
    return ref.get()