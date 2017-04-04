var nepalMap;
var spreadsheetID = "1mxcmAbjrVTU9c3zDy-Mz7PfziEtKNI1PejGuvwD4PW4";
var jsonurl = "https://spreadsheets.google.com/feeds/list/" + spreadsheetID + "/1/public/values?alt=json";
$.getJSON(jsonurl, function(datas) {
    $entrys = datas.feed.entry;
     $($entrys).each(function(){
        if(this.gsx$district.$t.toLowerCase()=="total") {
            if (this.gsx$nagarpalika.$t == '') {
                this.gsx$nagarpalika.$t = 0
            }
            if (this.gsx$gaupalika.$t == '') {
                this.gsx$gaupalika.$t = 0
            }
            if (this.gsx$upamahanarpalika.$t == '') {
                this.gsx$upamahanarpalika.$t = 0

            }
            if (this.gsx$mahanarpalika.$t == '') {
                this.gsx$mahanarpalika.$t = 0
            }
              if (this.gsx$totalnumberofregisteredvoters.$t == '') {
                this.gsx$mahanarpalika.$t = "NULL"
            }
            document.getElementById("nagar").innerHTML = this.gsx$nagarpalika.$t;
            document.getElementById("upnagar").innerHTML = this.gsx$upamahanarpalika.$t;
            document.getElementById("mahanagar").innerHTML = this.gsx$mahanarpalika.$t;
            document.getElementById("gau").innerHTML = this.gsx$gaupalika.$t;
            document.getElementById("tp").innerHTML = this.gsx$totalpopulation.$t;
            document.getElementById("rpp").innerHTML = this.gsx$registeredpoliticalparties.$t;
            document.getElementById("trv").innerHTML = this.gsx$totalnumberofregisteredvoters.$t;

        }

    });



});

function highlightFeature(e) {
    var layer = e.target;
    layer.setStyle(
        {
            weight: 1,
            color: 'black',
            fillColor: 'blue',
        }
    );
    if (!L.Browser.ie && !L.Browser.opera) {
        layer.bringToFront();
    }
}


function resetHighlight(e, feature) {
    nepalMap.resetStyle(e.target);
}

function zoomToFeature(e, feature) {

    map.fitBounds(e.target.getBounds());


}




function getUpdate(e) {
    $($entrys).each(function(){
        if(this.gsx$district.$t.toLowerCase()==e.toLowerCase()) {
            if (this.gsx$nagarpalika.$t == '') {
                this.gsx$nagarpalika.$t = 0
            }
            if (this.gsx$gaupalika.$t == '') {
                this.gsx$gaupalika.$t = 0
            }
            if (this.gsx$upamahanarpalika.$t == '') {
                this.gsx$upamahanarpalika.$t = 0

            }
            if (this.gsx$mahanarpalika.$t == '') {
                this.gsx$mahanarpalika.$t = 0
            }
            if (this.gsx$totalnumberofregisteredvoters.$t == '') {
                this.gsx$mahanarpalika.$t = "NULL"
            }            document.getElementById("nagar").innerHTML = this.gsx$nagarpalika.$t;
            document.getElementById("upnagar").innerHTML = this.gsx$upamahanarpalika.$t;
            document.getElementById("mahanagar").innerHTML = this.gsx$mahanarpalika.$t;
            document.getElementById("gau").innerHTML = this.gsx$gaupalika.$t;
            document.getElementById("district").innerHTML = e;
            document.getElementById("tp").innerHTML = this.gsx$totalpopulation.$t;
            document.getElementById("rpp").innerHTML = this.gsx$registeredpoliticalparties.$t;
            document.getElementById("trv").innerHTML = this.gsx$totalnumberofregisteredvoters.$t;



        }

    });

    }

function districtOnEachFeature(feature, layer) {
    layer.bindLabel(feature.properties.DISTRICT, {noHide: true});
    layer.on(
        {
            mouseover: highlightFeature,
            mouseout: resetHighlight,

        }
    );

    layer.on('click', function (e) {
        getUpdate(e.target.feature.properties.DISTRICT);
    });
}


function getProvinceColor(state) {
    if (state == 7) {
        return 'red';
    } else if (state == 6) {
        return '#c1a73e';
    } else if (state == 5) {
        return '#da8b4a';
    }
    else if (state == 4) {
        return '#26a9e8';
    }
    else if (state == 3) {
        return '#40a500';
    }
    else if (state == 2) {
        return '#e271a1';
    }
    else if (state == 1) {
        return '#900e94';
    }


}

function districtStyle(feature) {
    return {
        fillColor: getProvinceColor(feature.properties.PRADESH_NO),
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: 3,
        fillOpacity: 0.7
    }
}

var map = L.map('map',{
    minZoom: 6,
    maxZoom:10,
}).setView([43.8476, 18.3564], 3);



nepalMap = L.geoJson(
    geomap,
    {
        style: districtStyle,
        onEachFeature: districtOnEachFeature


    }
).addTo(map);

map.fitBounds(nepalMap.getBounds());


var legend = L.control({position : 'topright'});
			legend.onAdd = function(map){
				var div = L.DomUtil.create('div', 'legend');
				var labels = [
					"Province No. 1",
					"Province No. 2",
                    "Province No. 3",
					"Province No. 4",
                    "Province No. 5",
					"Province No. 6",
					"Province No. 7"
				];
				var grades = [1, 2, 3,4,5,6,7];
				div.innerHTML = '<div><h6>Province Index</h6></div>';
				for(var i = 0; i < grades.length; i++){
					div.innerHTML += '<i style="background:'
					+ getProvinceColor(grades[i]) + '">&nbsp;&nbsp;&nbsp;&nbsp;</i>&nbsp;&nbsp;'
					+ labels[i] + '<br />';
				}
				return div;
			}
			legend.addTo(map);

