## Drone Log

An app designed for drone pilots to log pre-flight checklists, flight logs, and maintenance.

## Technologies Used

Front end - React and CSS
Back end - Python and Django

## App features

- User authorization
- Users(pilots) can create a login and all of their data will be linked to their login
- Users can edit logs they created
- Users can delete logs they created

## Installation instructions

1. Fork this repo
2. Clone the repo
   `git clone [copied address]`
3. Install dependencies

## Models

```
class PreFlight(models.Model):
    pilot = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='preflights')
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    drone_reg = models.CharField(max_length=100)
    weather = models.TextField(blank=True)
    obstructions = models.TextField(blank=True)
    takeoff_clear = models.BooleanField(blank=False)

    def __str__(self):
        return f'{self.pilot.first_name} {self.pilot.last_name}, {self.location}, {self.date}, {self.time}'


class Flight(models.Model):
    preflight = models.ForeignKey(
        PreFlight, on_delete=models.CASCADE, related_name='flights')
    duration = models.CharField(max_length=100)
    incidents = models.TextField(blank=True)

    def __str__(self):
        return f'{self.location}, {self.date}, {self.time}'
```

## User Stories

As a user I want to have a login specifically for me so my records can only be edited by me.
As a user I want to be able to use a preflight checklist that is shown as completed by me and saved.
As a user I want an easy to use interface that allows me to record what is best practice per FAA guidelines.
As a user I want to be able to easily record flight information for storage in the case it is ever needed.
As a user I want to be able to record my drone maintenance and inspections so there is a record.
As a user I want a place to note all the things about my flights so I can come back to the information if needed.
