package main
import "fmt"
import ("time"
        "sync")
func main() {
    var wg sync.WaitGroup
    wg.Add(3)
//Create a new channel with make(chan val-type). Channels are typed by the values they convey.
    foundOreChan := make(chan string)
    minedOreChan := make(chan string)
//Send a value into a channel using the channel <- syntax. Here we send "ping" to the messages channel we made above, from a new goroutine.
    theMine := [5]string{"ore", "rock", "rock", "ore", "ore"}
    go Finder(foundOreChan, theMine, &wg)
//The <-channel syntax receives a value from the channel. Here we’ll receive the "ping" message we sent above and print it out.
    go Miner(foundOreChan, minedOreChan, &wg)
    go Smelter(minedOreChan, &wg)
    //doSomething()
    wg.Wait()
    fmt.Println("finished")
}


func Finder(outboundOreChan chan<- string, mine [5]string, wg *sync.WaitGroup){
    //wg.Add(1)
    for _, item := range mine {
        if item == "ore" {
            fmt.Println("Found ore!")
            outboundOreChan <- item
        }
    }
    close(outboundOreChan)
    wg.Done()
}

func Miner(inboundOreChan <-chan string, outboundOreChan chan<- string, wg *sync.WaitGroup){
     //wg.Add(1)
    for elem := range inboundOreChan {
        fmt.Println("mined element: ",elem, " sending to smelter")
        outboundOreChan <- elem
    }
    close(outboundOreChan)
    wg.Done()
}

func Smelter(inboundOreChan <-chan string, wg *sync.WaitGroup){
    //wg.Add(1)
    for elem := range inboundOreChan {
        fmt.Println("smelted element: ",elem)
    }
    wg.Done()
}
func doSomething() {
     for i := 0; i < 10; i++ {
        fmt.Println("Waiting for goroutines to finish...")
        time.Sleep(time.Second)
     }
    
     
}