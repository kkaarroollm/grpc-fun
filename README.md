### fun with grpc

1. ```POST /api/v1/bookings```
    - Example payload:
    ```json
       {
          "flight": {
            "class_": "economy",
            "food": "standard",
            "luggage": {
              "checked": true,
              "quantity": 2
            }
          },
          "hotel": {
            "stars": 4,
            "all_inclusive": true,
            "room_service": true,
            "airport_shuttle": false
          }
        }
   
    ```

2. Grpc on ports 50051 and 50052 for hotel and flight services respectively.
