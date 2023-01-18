function getTime() {
    $.ajax({
        url: '/time',
        timeout: 10000,
        success: function (data) {
            $("#time").html(data);
        },
        error: function (err, type, errorThrown) {
            console.log(err);
        }
    })
}

function getNum() {
    $.ajax({
        url: '/num',
        timeout: 10000,
        success: function (data) {
            let num = $(".num h1");
            num.eq(0).text(data.pokemon);
            num.eq(1).text(data.skill);
            num.eq(2).text(data.ability);
            num.eq(3).text(data.gen);
        },
        error: function (err, type, errorThrown) {
            console.log(err);
        }
    })
}

function getC1() {
    $.ajax({
        url: '/type',
        timeout: 10000,
        success: function (data) {
            let result = [];
            for (let val in data) {
                let k = val;
                let v = data[val];
                let obj = {value: v.toString(), name:k.toString()};
                result.push(obj);
            }
            ec_left1_options.series[0].data = result;
            ec_left1.setOption(ec_left1_options);
        },
        error: function (err, type, errorThrown) {
            console.log(err);
        }
    })
}

function getC2() {
    $.ajax({
        url: '/gen',
        timeout: 10000,
        success: function (data) {
            ec_left2_options.xAxis[0].data = data.gen;
            ec_left2_options.series[0].data = data.pokemon;
            ec_left2_options.series[1].data = data.skill;
            ec_left2_options.series[2].data = data.ability;
            ec_left2.setOption(ec_left2_options);
        },
        error: function (err, type, errorThrown) {
            console.log(err);
        }
    })
}

getNum();
getC1();
getC2();
setInterval(getTime, 1000);