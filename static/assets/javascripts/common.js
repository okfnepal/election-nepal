// Copyright (c) 2013 Ryan Clark
    // https://gist.github.com/rclark/5779673
    L.TopoJSON = L.GeoJSON.extend({
        addData: function (jsonData) {
            if (jsonData.type === "Topology") {
                for (key in jsonData.objects) {
                    geojson = topojson.feature(jsonData, jsonData.objects[key]);
                    L.GeoJSON.prototype.addData.call(this, geojson);
                }
            }
            else {
                L.GeoJSON.prototype.addData.call(this, jsonData);
            }
        }
    });



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


     (function () {
        var map = L.map('map', {maxZoom:  7.9, minZoom:  6.9 }),
            topoLayer = new L.TopoJSON(),
            colorScale = chroma
                .scale(['#D5E3FF', '#003171'])
                .domain([0, 1]);
                 map.dragging.disable();

        map.setView([28.1999999, 84.100140],  6.9);

        $.getJSON('static/assets/javascripts/nepal-districts.topo.json').done(addTopoData);

        function addTopoData(topoData) {
            topoLayer.addData(topoData);
            topoLayer.addTo(map);
            topoLayer.eachLayer(handleLayer);
        }


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

        function resetHighlight(e) {
            var layer = e.target;
            var setColor=layer.feature.properties.pradesh_no
            layer.setStyle(
                {
                    fillColor: getProvinceColor(setColor),
                    weight: 2,
                    opacity: 1,
                    color: 'white',
                    dashArray: 3,
                    fillOpacity: 0.7
                }
            );

            if (!L.Browser.ie && !L.Browser.opera) {
                layer.bringToFront();
            }
        }



        function handleLayer(layer) {
            layer.bindLabel(layer.feature.properties.name, {noHide: true})
            var code = layer.feature.properties.name;
            var setColor=layer.feature.properties.pradesh_no;
            layer.setStyle({
                fillColor: getProvinceColor(setColor),
                weight: 2,
                opacity: 1,
                color: 'white',
                dashArray: 3,
                fillOpacity: 0.7
            });
            layer.on({
                mouseover: highlightFeature,
                mouseout: resetHighlight,

            });

            layer.on('click', function (e) {
                 getUpdate(layer.feature.properties.name);
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


        var legend = L.control({position: 'topright'});
        legend.onAdd = function (map) {
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
            var grades = [1, 2, 3, 4, 5, 6, 7];
            div.innerHTML = '<div><h6>Province Index</h6></div>';
            for (var i = 0; i < grades.length; i++) {
                div.innerHTML += '<i style="background:'
                    + getProvinceColor(grades[i]) + '">&nbsp;&nbsp;&nbsp;&nbsp;</i>&nbsp;&nbsp;'
                    + labels[i] + '<br />';
            }
            return div;
        }
        legend.addTo(map);

    }());
