db.createCollection('local', {
  validator: {
    $jsonSchema: {
      bsonType: 'object',
      title: 'local',
      required: ['name'],
      properties: {
        name: {
          bsonType: 'string'
        },
        purification_plant: {
          bsonType: 'array',
          items: {
            title: 'wide_water_purification_plant',
            required: ['purification', 'date', 'taste', 'smell', 'color', 'pH', 'NTU', 'residual_chlorine'],
            properties: {
              purification: {
                bsonType: 'string'
              },
              date: {
                bsonType: 'string'
              },
              taste: {
                bsonType: 'string'
              },
              smell: {
                bsonType: 'string'
              },
              color: {
                bsonType: 'double'
              },
              pH: {
                bsonType: 'double'
              },
              NTU: {
                bsonType: 'double'
              },
              residual_chlorine: {
                bsonType: 'double'
              }
            }
          }
        },
        multiPurpose_dam: {
          bsonType: 'array',
          items: {
            title: 'multiPurpose_dam',
            required: ['dam', 'month', 'pH', 'DO', 'BOD', 'COD', 'NTU'],
            properties: {
              dam: {
                bsonType: 'string'
              },
              month: {
                bsonType: 'string'
              },
              pH: {
                bsonType: 'double'
              },
              DO: {
                bsonType: 'double'
              },
              BOD: {
                bsonType: 'double'
              },
              COD: {
                bsonType: 'double'
              },
              NTU: {
                bsonType: 'double'
              }
            }
          }
        }
      }
    }
  }
});
