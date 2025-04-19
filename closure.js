// 즉, 반환당시 함수의 유효범위를 벗어난 변수 또는 메서드에 접근이 된다!! (소멸되지 않은 것임.)

// const closure_avg = () => {
//     // 이 영역을 뭐라고 부르지?
//     // 렉시컬 환경 혹은 클로저 스코프
//     series = []

//     const averager = (v) => {
//         series.push(v)
//         console.log(`def >>> ${series} / ${series.length}`)
//         return Number(series.reduce((a, b) => (a + b)) / series.length)
//     }
//     return averager
// }
// const tmp = closure_avg()

// console.log(tmp(1))
// console.log(tmp(2))
// console.log(tmp(3))

function friend() {
    let friends = []

    function add_friend(name) {
        friends.push(name)
        console.log(friends)
    }

    return add_friend
}

const closure = friend()
closure("김철수") // [ '김철수' ]
closure("박영희") // [ '김철수', '박영희' ]
closure("홍길동") // [ '김철수', '박영희', '홍길동' ]

// 중복 제거
// 클로저보다 문법이 간결

// 에러 추적 힘듦
// 에러 발생 지점 추적 모호
// 디버깅 힘들다!