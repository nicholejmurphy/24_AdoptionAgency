from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

buddy = Pet(name='Buddy', species='Cat', age=12,
            notes='A great pal for some loving cat owners. Loves playing with the fishing pole and feather. Big lover...on his own time.', available=True)
squirrel = Pet(name='Spencer', species='Squirrel', age=3,
               notes='A little nuts, but could be the right companion for you!', available=True)
fish = Pet(name='Bubbles', species='Fish', age=1,
           notes='Loves tv and yummy snacks. Enjoys seaweed cuddles and rom-coms.', available=True)
iggy = Pet(name='Iggy', species='Iguana', age=4,
           notes='Not the best lap pet. Loves a good adventure and playing princess dress-up.', available=True)
James = Pet(name='James', species='Owl', age=5,
            notes='Very wise lad. Loves a good night time read and staying updated with NPR.', available=True)
Jess = Pet(name='Jessssss', species='Snake', age=4,
           notes='A vegitarian. Working to end world hunger.', available=True)
Karl = Pet(name='Karl', species='Mouse', age=1,
           notes='Sneaky guy, probably means well. Needs a good home.', available=True)
pj = Pet(name='PB&J', species='Cat', age=6,
         notes='A great freind. Comes when called. Loves naps in the sun.', available=False)
Jack = Pet(name='Jack', species='Cat', age=13,
           notes='THE most friendly cat you will ever meet.', available=False)
Moon = Pet(name='Moon', species='Dog', age=3,
           notes='High energy and loves to play. Will win your heart if you let him!', available=False)

db.session.add(buddy)
db.session.add(squirrel)
db.session.add(fish)
db.session.add(iggy)
db.session.add(James)
db.session.add(Jess)
db.session.add(Karl)
db.session.add(pj)
db.session.add(Jack)
db.session.add(Moon)

db.session.commit()
