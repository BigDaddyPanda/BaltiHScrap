from pyyoutube import Api
api = Api(api_key='AIzaSyD5GHt7wRfRbrl6gkpX0612SB1xkj2gqDw')



r = api.get_subscription_by_me(
         parts=["id", "snippet"],
         count=2
    )
print(r.items)