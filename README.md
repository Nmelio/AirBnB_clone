# HBnB The Console Project - An AirBnB Clone
## Project Description:


HBnB is a Python-based command interpreter inspired by Airbnb's platform, designed to replicate its functionality. Operating through a user-friendly command-line interface, the console empowers users to seamlessly engage with the Airbnb's clone intricate data models, enabling a diverse range of actions and interactions.

### Getting Started:

To launch the HBnB console, just follow these simple steps:

1. Clone the project repository:
   ```git clone https://github.com/prosperemebo/AirBnB_clone/```

2. Navigate to the project directory:
   ```cd AirBnB_clone```

3. Launch the console:
   ```./console.py```

## Usage:

The console provides a range of commands that enable you to manipulate data models, execute operations, and engage with HBnB features. Here are a few sample commands along with their usage:

### Creating a New Object:

Using the 'create' command, you have the option to generate any of the 7 new model objects: `BaseModel, User, Place, State, City, Amenity, or Review`. The console will handle the creation process by assigning a unique ID to the new instance and subsequently presenting it.

	(hbnb) create User
	c090ad70-7bf9-4ee4-b670-778287da1f93
	(hbnb) create Amenity
	184a462a-1093-4301-b78c-73bc569d097f

### Listing Objects:

You can display a list of objects belonging to a particular class:

	(hbnb) all Amenity
	["[Amenity] (0a0d1744-5114-4b46-90ba-4da6ca39ea1e) {'id': '0a0d1744-5114-4b46-90ba-4da6ca39ea1e', 'created_at': datetime.datetime(2023, 8, 11, 12, 17, 35, 957610), 'updated_at': datetime.datetime(2023, 8, 11, 12, 17, 35, 957697)}", "[Amenity] (184a462a-1093-4301-b78c-73bc569d097f) {'id': '184a462a-1093-4301-b78c-73bc569d097f', 'created_at': datetime.datetime(2023, 8, 13, 0, 10, 54, 789947), 'updated_at': datetime.datetime(2023, 8, 13, 0, 10, 54, 790023)}"]

Or by using: ```<class name>.all()```

	(hbnb) Amenity.all()
	["[Amenity] (0a0d1744-5114-4b46-90ba-4da6ca39ea1e) {'id': '0a0d1744-5114-4b46-90ba-4da6ca39ea1e', 'created_at': datetime.datetime(2023, 8, 11, 12, 17, 35, 957610), 'updated_at': datetime.datetime(2023, 8, 11, 12, 17, 35, 957697)}", "[Amenity] (184a462a-1093-4301-b78c-73bc569d097f) {'id': '184a462a-1093-4301-b78c-73bc569d097f', 'created_at': datetime.datetime(2023, 8, 13, 0, 10, 54, 789947), 'updated_at': datetime.datetime(2023, 8, 13, 0, 10, 54, 790023)}"]

### Updating an Object:

You can modify an object's attributes individually by using the 'update' command, followed by the class name, object ID, attribute name, and attribute value:

	(hbnb) update User c17fcbe9-c4b6-49b0-bc1f-835d0efc655b email "aibnb@mail.com"

Or by using ```<class name>.update(<id>, <attribute name>, <attribute value>)``` or ```<class name>.update(<id>, <dictionary representation>)``` to update multiple attributes at a time:

	(hbnb) User.update("c17fcbe9-c4b6-49b0-bc1f-835d0efc655b", "first_name", "Betty", "age", 24, "budget", "400$")

### Displaying Object Details:

Using the 'show' command, you can view all attributes of an object by providing its class name and ID:

	(hbnb) show User c17fcbe9-c4b6-49b0-bc1f-835d0efc655b
	[User] (c17fcbe9-c4b6-49b0-bc1f-835d0efc655b) {'id': 'c17fcbe9-c4b6-49b0-bc1f-835d0efc655b', 'created_at': datetime.datetime(2023, 8, 9, 13, 25, 23, 943809), 'updated_at': datetime.datetime(2023, 8, 13, 0, 15, 18, 743903), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'aibnb@mail.com', 'password': 'root', '"first_name"': 'Betty'}

Or by using ```<class name>.show(<id>)```:

	(hbnb) User.show(c17fcbe9-c4b6-49b0-bc1f-835d0efc655b)
	[User] (c17fcbe9-c4b6-49b0-bc1f-835d0efc655b) {'id': 'c17fcbe9-c4b6-49b0-bc1f-835d0efc655b', 'created_at': datetime.datetime(2023, 8, 9, 13, 25, 23, 943809), 'updated_at': datetime.datetime(2023, 8, 13, 0, 15, 18, 743903), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'aibnb@mail.com', 'password': 'root', '"first_name"': 'Betty'}

### Deleting an Object:

Use the 'destroy' command along with the class name and object ID to remove an object:

   	(hbnb) destroy User c17fcbe9-c4b6-49b0-bc1f-835d0efc655b

Or by using ```<class name>.destroy(<id>)```:

	(hbnb) User.destroy(c17fcbe9-c4b6-49b0-bc1f-835d0efc655b)

### Counting instances of a Class:

You can find the instance count of a class using the ```<class name>.count()``` command:

	(hbnb) User.count()
	9
