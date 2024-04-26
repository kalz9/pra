import java.rmi.Remote;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class ConcatenationServer {
    public interface ConcatenationService extends Remote {
        String concatenateStrings(String str1, String str2) throws RemoteException;
    }

    public static class ConcatenationServiceImpl extends UnicastRemoteObject implements ConcatenationService {
        protected ConcatenationServiceImpl() throws RemoteException {
            super();
        }

        @Override
        public String concatenateStrings(String str1, String str2) throws RemoteException {
            System.out.println("String one received: " + str1);
            System.out.println("String two received: " + str2);
            return str1 + str2;
        }
    }

    public static void main(String[] args) {
        try {
            ConcatenationService service = new ConcatenationServiceImpl();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("ConcatenationService", service);
            System.out.println("Server is running...");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
