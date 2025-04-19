class Friend{
    friends = []

    add_friend(name) {
        this.friends.push(name);
        console.log(this.friends);
    }
}

const friend = new Friend();
friend.add_friend("김철수") // [ '김철수' ]
friend.add_friend("박영희") // [ '김철수', '박영희' ]
friend.add_friend("홍길동") // [ '김철수', '박영희', '홍길동' ]