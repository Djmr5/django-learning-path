import requests, argparse, json

# Make request to server
def make_request(request_type, endpoint, data=None):
    """
    Function to make request to server based on the passed parameters
    """

    # Check request type
    if request_type == "GET":
        response = requests.get(endpoint, json=data)
    elif request_type == "POST":
        response = requests.post(endpoint, json=data)
    elif request_type == "PUT":
        response = requests.put(endpoint, json=data)
    elif request_type == "DELETE":
        response = requests.delete(endpoint, json=data)
    else:
        # Invalid request type
        response = None

    # Return response
    return response

# Main function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Client emulator to send requests to an API endpoint",
        epilog="Made by: Diego Jacobo M. - Github: @Djmr5"
    )
    # Arguments
    # Request type arg
    parser.add_argument(
        "-t", "--type",
        type=str,
        choices=["GET", "POST", "PUT", "DELETE"],
        default="GET",
        help="Request type to send to server (GET, POST, PUT, DELETE)",
    )
    # Endpoint arg
    parser.add_argument(
        "-e", "--endpoint",
        type=str,
        required=True,
        help="Endpoint to send request to (Full URL)",
    )
    # Data arg
    parser.add_argument(
        "-d", "--data",
        type=str,
        help="Data file to send to server (JSON format), must be a valid JSON file (.json)",
    )

    # Parse arguments
    args = parser.parse_args()

    # Check if data arg is passed
    if args.data and args.data.endswith(".json"):
        # Open data file
        try:
            with open(args.data, "r") as file:
                # Load data
                data = json.load(file)
            # Make request
            response = make_request(args.type, args.endpoint, data)
        except:
            # Print error
            print("An error ocurred while opening the data file")
            response = None
    else:
        # Make request
        response = make_request(args.type, args.endpoint)

    # Check if response is not None
    if response:
        # Print response
        print(response.json())
        print(response.text)
        print(response.status_code)
    else:
        # Print error
        print("Invalid request type")