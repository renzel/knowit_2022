let prøve_antall_kort = 10000

function stitch(x: number[], y: number[]) {
    let arr: number[] = [];
    let length = Math.max(x.length, y.length);
    for(let l = 0; l < length; l++) {
      l < x.length && arr.push(x[l]);
      l < y.length && arr.push(y[l]);
    }
    return arr;
  }
for (let i = 1; i <= prøve_antall_kort; i++) {
    if (i % 2 == 0){
    
        let kortstokk: number[]  = []
        for (let x:number = 1; x <= i; x++) {
            kortstokk.push(x);
        };
        //console.log(kortstokk)
        let før_shuffle: number[] = kortstokk;
        let valid: Boolean = true;
        for (let n:number = 0; n <= 12; n++) {
            const først_halvdel: number[] = kortstokk.slice(0,kortstokk.length/2);
            const andre_halvdel: Array<number> = kortstokk.slice(kortstokk.length/2, kortstokk.length);
            kortstokk = stitch(først_halvdel, andre_halvdel);
            if (kortstokk.every((v,i)=> v === før_shuffle[i]) && n != 12)
                valid = false
         
           
        }
        if (kortstokk.every((v,i)=> v === før_shuffle[i]) && valid) {
            
            console.log(i);
            console.log(kortstokk);
            break;
        }
        
            
    }
}
console.log("DONE"); 

/*prøve_antall_kort = 10000
for i in range(1, prøve_antall_kort):
    if i % 2 == 0:
        kortstokk = []
        for x in range(1, i + 1):
            kortstokk.append(x)
        før_shuffle = kortstokk
        valid = True
        #print()
        #print(kortstokk)
        for n in range(13):
            midten = int(len(kortstokk)/2)

            først_halvdel = kortstokk[:midten]
            andre_halvdel = kortstokk[midten:]

            result = [None]*(len(først_halvdel)+len(andre_halvdel))
            result[::2] = først_halvdel
            result[1::2] = andre_halvdel
            kortstokk = result
            if kortstokk == før_shuffle and n != 12:
                valid = False
        if kortstokk == før_shuffle and valid:
            print(i)
            print(kortstokk)
            break
        
# print(kortstokk)*/