import requests



base_url = 'http://127.0.0.1:8000/'
class CreatedComments:
    @staticmethod
    def created_comments(authorization, id):
        path_post = 'api/comments/'
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {authorization}"

        }
        json_body = {
                "post": id,
                "text": "Hello"
        }
        post_url = base_url + path_post
        res_post = requests.post(post_url, headers=headers, json=json_body)
        print(res_post.text)
        return res_post