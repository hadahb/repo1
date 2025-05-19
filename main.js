const userRecords=[
    {"name": "Jessica", "points": 78, "position": 2},
    {"name": "Kelvin", "points": 70, "position": 3},
    {"name": "Davie", "points: 88, position: 1},
    {name: "Benny", points: 69, position: 4}
];
const newINFO = [];

const ans = JSON.parse(userRecords, function reviver(key, value)
{
    i=0;
    if(key === 'name'){
        while(i<4){
            newINFO.push(userRecords[i].points)= value;
        }
        i++;
    } 
    return userRecords[i].points; 
});
console.log(newINFO);